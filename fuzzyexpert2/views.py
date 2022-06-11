import re
from django.shortcuts import render
from .models import Student
from .fls_main import calculate_FLS

def index(request):
    return render(request, 'study_main.html')

def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
    return render(request, 'study_conclusion.html', students)

def result(request):
    if request.method == "POST":
        fio = request.POST.get("student_fio")
        age = request.POST.get("student_age")
        group = request.POST.get("student_group")
        lecture = request.POST.get("student_lectureSlider")
        practic = request.POST.get("student_practicSlider")
        project = request.POST.get("student_projectSlider")
        visits = request.POST.get("student_visitsSlider")
        result  = calculate_FLS(float(lecture), float(practic), float(project), float(visits))
        new_student  = Student.objects.create(
            fio = fio,
            age = age,
            group = group,
            lecture = lecture,
            practic = practic,
            project = project,
            visits = visits,
            score = result
        )
        new_student.save()    
        students = Student.objects.all()
    return render(request, 'study_conclusion.html', {'res': result,'fio': fio, 'students': students})  