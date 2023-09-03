from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_school(request):
    if request.method=='POST':
        scn=request.POST['scn']
        sp=request.POST['sp']
        sl=request.POST['sl']

        so=School.objects.get_or_create(ScName=scn,ScPrincipal=sp,ScLocation=sl)[0]
        so.save()
        QLSO=School.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_schools.html',d)
    return render(request,'insert_school.html')

def insert_student(request):
    if request.method=='POST':
        scn=request.POST['scn']
        stn=request.POST['stn']
        si=request.POST['si']
        so=School.objects.get(ScName=scn)
        sto=Student.objects.get_or_create(ScName=so,Sname=stn,Sid=si)[0]
        sto.save()

        QLSTO=Student.objects.all()
        d={'QLSTO':QLSTO}
        return render(request,'display_students.html',d)
    return render(request,'insert_student.html')