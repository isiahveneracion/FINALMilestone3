# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_table, name='student_table'),  # URL for the homepage (student table)
    path('add/', views.add_student, name='add_student'),  # URL for adding a student
]
