import re
from django.shortcuts import render

from .search import Curb, Port, Smart
from .models import Patient
from .fls_main import calculate_FLS
# , plot_cough_mf,plot_fever_mf, plot_additional_mf, plot_breathdiff_mf, plot_risk_mf

def index(request):
    return render(request, 'covidmain.html')


def patient_list(request):
    if request.method == "GET":
        patients = Patient.objects.all()
    
    return render(request, 'covid19.html', patients)


def c19(request):
    if request.method == "POST":
        name = request.POST.get("patient_name")
        age = request.POST.get("age1")
        cough = request.POST.get("coughSlider")
        fever = request.POST.get("feverSlider")
        breath = request.POST.get("breathSlider")
        polluted = request.POST.get("polluted")
        hypertension = request.POST.get("hypertension")
        diabet = request.POST.get("diabet")
        cardio = request.POST.get("cardio")
        respiratory = request.POST.get("respiratory")
        immune = request.POST.get("immune")

        result  = calculate_FLS(float(cough), float(fever), float(breath), int(age), int(polluted),
        int(hypertension), int(diabet), int(cardio), int(respiratory), int(immune))
        
        new_patient  = Patient.objects.create(
            name = name,
            age = age,
            c19_result = result
        )
        new_patient.save()    

        patients = Patient.objects.all()
    return render(request, 'covid19.html', {'res': result,'name': name, 'patients': patients})  


def result(request):
    if request.method == "POST":
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        p0 = request.POST.get("p0")
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        p3 = request.POST.get("p3")
        p4 = request.POST.get("p4")
        p5 = request.POST.get("p5")
        p6 = request.POST.get("p6")
        p7 = request.POST.get("p7")
        p8 = request.POST.get("p8")
        p9 = request.POST.get("p9")
        p10 = request.POST.get("p10")
        p11 = request.POST.get("p11")
        p12 = request.POST.get("p12")
        p13 = request.POST.get("p13")
        p14 = request.POST.get("p14")
        p15 = request.POST.get("p15")
        p16 = request.POST.get("p16")
        p17 = request.POST.get("p17")
        s1 = request.POST.get("s1")
        s2 = request.POST.get("s2")
        s3 = request.POST.get("s3")
        port_r = Port( p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, sex, age)
        res = port_r.get_result()

        curb_c = Curb(age ,p6, p12, p8, p9)
        res_c = curb_c.get_result()

        smart_s = Smart(p9, s1, s2, p8, p7, p6, s3, p11)
        res_s = smart_s.get_result()



        return render(request, 'result.html', {'res': res, 'res_c': res_c, 'res_s':res_s})