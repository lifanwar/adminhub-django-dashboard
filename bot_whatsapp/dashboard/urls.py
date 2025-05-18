from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('get-qr-code/', views.get_qr_code, name='get_qr_code'),
    path('disconnect/', views.disconnect, name='disconnect'),
]
