from django.urls import path
from .views import students, studentdetail, searchstudents

urlpatterns = [
    path('students/', students),
    path('students/<int:rolno>/', studentdetail),
    path('search/', searchstudents),
]
