from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            student = Student(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                course=form.cleaned_data["course"],
                gender=form.cleaned_data["gender"],
                age=form.cleaned_data["age"],
            )
            student.save()
            return HttpResponse(f"Thank you, {first_name}")
    else:
        form = StudentForm()
    
    context = {"form": form}
    return render(request, "student_form.html", context)

def student_table(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_table.html', context)