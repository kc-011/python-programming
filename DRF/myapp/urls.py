from django.urls import path
from .views import students, studentdetail

urlpatterns = [
    path('students/', students),
    path('students/<int:rolno>/', studentdetail),
]
