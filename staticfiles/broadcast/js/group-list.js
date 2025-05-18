function groupList() {
    return {
        groups: [],
        filteredGroups: [],
        selectedGroups: [],
        searchQuery: '',
        selectAll: false,
        isFetched: false, // Track if groups were just fetched

        init() {
            // Only load saved groups on init
            const savedGroups = localStorage.getItem('savedWhatsappGroups');
            if (savedGroups) {
                try {
                    this.groups = JSON.parse(savedGroups);
                    this.filterGroups();
                } catch (e) {
                    console.error('Error parsing saved groups:', e);
                    localStorage.removeItem('savedWhatsappGroups');
                }
            }

            // Watch selectedGroups changes to update selectAll state
            this.$watch('selectedGroups', value => {
                // Update selectAll based on whether all filtered groups are selected
                this.selectAll = value.length > 0 && value.length === this.filteredGroups.length;
            });

            // Clear fetched groups on page refresh if they weren't saved
            window.addEventListener('beforeunload', () => {
                if (this.isFetched && !this.hasSelectedGroups) {
                    this.groups = [];
                    this.filterGroups();
                }
            });
        },

        async fetchGroups() {
            // Always show loading state when explicitly fetching
            window.dispatchEvent(new CustomEvent('loading-start'));
            
            // Clear existing groups and selection before fetching
            this.groups = [];
            this.selectedGroups = [];
            this.selectAll = false;
            this.filterGroups();
            
            // Set up timeout
            const timeoutPromise = new Promise((_, reject) => {
                setTimeout(() => {
                    reject(new Error('Request timed out. The server is taking longer than expected to respond. Please try again.'));
                }, 45000); // 45 seconds timeout
            });

            try {
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                const fetchPromise = fetch('/broadcast/fetch-groups/', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json',
                    },
                    credentials: 'same-origin'
                });

                // Race between fetch and timeout
                const response = await Promise.race([fetchPromise, timeoutPromise]);
                
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || `Server error: ${response.status}`);
                }
                
                const data = await response.json();
                if (data.error) {
                    throw new Error(data.error);
                }
                
                this.groups = data.groups || [];
                this.filterGroups();
                this.isFetched = true; // Mark as fetched
                window.dispatchEvent(new CustomEvent('notification', { 
                    detail: { 
                        message: `Successfully fetched ${this.groups.length} groups`, 
                        type: 'success' 
                    }
                }));
            } catch (error) {
                window.dispatchEvent(new CustomEvent('notification', { 
                    detail: { 
                        message: error.message || 'Failed to fetch groups', 
                        type: 'error' 
                    }
                }));
            } finally {
                window.dispatchEvent(new CustomEvent('loading-end'));
            }
        },

        async saveSelectedGroups() {
            if (this.selectedGroups.length === 0) return;

            try {
                // Get the selected group objects
                const selectedGroupObjects = this.groups.filter(group => 
                    this.selectedGroups.includes(group.id)
                );

                const response = await fetch('/broadcast/save-groups/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    },
                    body: JSON.stringify(this.selectedGroups)
                });
                
                const data = await response.json();
                if (data.status === 'success') {
                    // Save selected groups to localStorage
                    localStorage.setItem('savedWhatsappGroups', JSON.stringify(selectedGroupObjects));
                    
                    // Update state
                    this.groups = selectedGroupObjects;
                    this.selectedGroups = [];
                    this.selectAll = false;
                    this.isFetched = false; // Reset fetched state
                    this.filterGroups();

                    window.dispatchEvent(new CustomEvent('notification', { 
                        detail: { 
                            message: `Successfully saved ${selectedGroupObjects.length} groups`, 
                            type: 'success' 
                        }
                    }));
                } else {
                    throw new Error(data.message);
                }
            } catch (error) {
                window.dispatchEvent(new CustomEvent('notification', { 
                    detail: { message: error.message || 'Failed to save groups', type: 'error' }
                }));
            }
        },

        filterGroups() {
            if (!this.searchQuery) {
                this.filteredGroups = this.groups;
            } else {
                const query = this.searchQuery.toLowerCase();
                this.filteredGroups = this.groups.filter(group => 
                    group.name.toLowerCase().includes(query) ||
                    group.id.toLowerCase().includes(query)
                );
            }
        },

        toggleAll() {
            // Toggle based on current selectAll state
            if (!this.selectAll) {
                // If not all selected, select all filtered groups
                this.selectedGroups = this.filteredGroups.map(group => group.id);
            } else {
                // If all selected, deselect all
                this.selectedGroups = [];
            }
            // Update selectAll state
            this.selectAll = !this.selectAll;
        },

        get hasSelectedGroups() {
            return this.selectedGroups.length > 0;
        }
    }
}
