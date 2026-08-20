from django.urls import path, include
from .views import home, contact, register

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact),
    path('register/', register, name='register'),
    path('auth/', include('django.contrib.auth.urls')),
]
