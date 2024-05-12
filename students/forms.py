from django import forms

COURSES = (
    ("BS-CS", "Computer Science"),
    ("BS-DS", "Data Science"),
    ("BS-IS", "Information Systems"),
    ("BS-IT", "Information Technology"),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class StudentForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    course = forms.ChoiceField(choices=COURSES, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, required=True)
    age = forms.IntegerField(required=True)
