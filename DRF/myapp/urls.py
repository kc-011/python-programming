from django.urls import path
from .views import students, studentdetail, searchstudents, StudentsAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', students),
    path('students/<int:rolno>/', studentdetail),
    path('search/', searchstudents),
    path('class-students/', StudentsAPIView.as_view()),
    path('class-students/<int:rolno>/', StudentDetailAPIView.as_view()),
]
