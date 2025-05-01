from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('agent/dashboard/', views.agent_dashboard, name='agent_dashboard'),
    path('request/create/', views.create_service_request, name='create_service_request'),
    path('request/<int:request_id>/<str:status>/', views.update_request_status, name='update_request_status'),
    path('chat/<int:request_id>/', views.chat, name='chat'),
]