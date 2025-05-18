from django.urls import path
from . import views

app_name = 'broadcast'

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('fetch-groups/', views.fetch_groups, name='fetch_groups'),
    path('save-groups/', views.save_groups, name='save_groups'),
]
