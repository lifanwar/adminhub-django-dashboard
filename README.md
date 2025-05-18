# AdminHub - Django Dashboard

A modern admin dashboard built with Django and Tailwind CSS, inspired by the AdminHub template. This dashboard provides a clean and responsive interface for managing your application.

## Features

- 📱 Fully responsive design that works on desktop, tablet, and mobile
- 🎨 Modern UI with Tailwind CSS
- 📊 Interactive charts using Chart.js
- 🔍 Real-time search functionality
- 📱 Mobile-friendly navigation with collapsible sidebar
- 🎯 Clean and intuitive user interface
- 📊 Statistics cards with trend indicators
- 📈 Sales and revenue visualization
- 👥 Recent buyers tracking
- 💳 Transaction monitoring

## Tech Stack

- Django 5.2
- Tailwind CSS
- Alpine.js for interactive components
- Chart.js for data visualization
- Google Fonts (Inter)

## Getting Started

1. Clone the repository
```bash
git clone <repository-url>
cd adminhub
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install django
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Visit http://localhost:8000 in your browser

## Project Structure

```
adminhub/
├── core/                   # Project settings and main URLs
├── dashboard/             # Main dashboard application
│   ├── templates/        # HTML templates
│   │   ├── components/  # Reusable template components
│   │   └── dashboard/   # Dashboard-specific templates
│   ├── views.py         # View controllers
│   └── urls.py          # URL routing
├── static/               # Static files (CSS, JS, images)
└── manage.py            # Django management script
```

## Customization

The dashboard is built with customization in mind:

- Colors and theme can be adjusted in the Tailwind configuration
- Components are modular and can be easily modified
- Charts can be customized to display your own data
- Sidebar menu items can be added or removed as needed

## Browser Support

The dashboard is compatible with all modern browsers:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
