from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    COURSES = (
        ("BS-CS", "Computer Science"),
        ("BS-DS", "Data Science"),
        ("BS-IS", "Information Systems"),
        ("BS-IT", "Information Technology"),
    )
    course = models.CharField(max_length=4)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
