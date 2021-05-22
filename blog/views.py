from django.http import HttpResponseRedirect

from django.shortcuts import render
from datetime import datetime
from .models import Subscribe
from .models import Contact 
from .models import Teacher_Sign
from .models import Student_Sign
from django.contrib import messages
from .forms import UploadFileForm


def homepage(request):
    if request.method =="POST":
        if 'contact' in request.POST:
            name=request.POST.get('Name')
            email=request.POST.get('Email') 
            message=request.POST.get('Message')
            contact=Contact(name=name,email=email,message=message ,date=datetime.today())
            contact.save()
            messages.success(request,'Your Message has been sent')
        else:
            name=request.POST.get('name')
            email=request.POST.get('email')
            subscribe=Subscribe(name=name,email=email,date=datetime.today())
            subscribe.save()
            messages.success(request,'You have sucessfully subscribed')
    return render(request,'index.html')


def teacher_sign(request):
    if request.method =="POST":
            name=request.POST.get('Name')
            email=request.POST.get('Email') 
            address=request.POST.get('Address')
            phone=request.POST.get('Phone')
            city=request.POST.get('City')
            country=request.POST.get('Country')
            zip=request.POST.get('Zip')
            #photo=request.POST.get('Photo')
            degree=request.POST.get('Degree')
            university=request.POST.get('College')
            #certificate=request.POST.get('Certificate')
            subject=request.POST.get('Subject')
            experience=request.POST.get('Experience')
            week=request.POST.get('Week')
            medium=request.POST.get('Medium')
            Teacher=Teacher_Sign(name=name,email=email,address=address,phone=phone,city=city,country=country,zip=zip,degree=degree,university=university,subject=subject,experience=experience,week=week,medium=medium ,date=datetime.today())
            Teacher.save()
            messages.success(request,'Your account has been created.You will be emailed as soon as the student is avaliable')
            return render(request,'index.html',locals())
    return render(request,'teacher_sign.html',locals())

def student_sign(request):
    if request.method =="POST":
            name=request.POST.get('Name')
            email=request.POST.get('Email') 
            address=request.POST.get('Address')
            phone=request.POST.get('Phone')
            city=request.POST.get('City')
            country=request.POST.get('Country')
            zip=request.POST.get('Zip')
            #photo=request.POST.get('Photo')
            degree=request.POST.get('Degree')
            school=request.POST.get('School')
            #marksheet=request.POST.get('Marksheet')
            subject=request.POST.get('Subject')
            experience=request.POST.get('Experience')
            week=request.POST.get('Week')
            medium=request.POST.get('Medium')
            Student=Student_Sign(name=name,email=email,address=address,phone=phone,city=city,country=country,zip=zip,degree=degree,school=school,subject=subject,experience=experience,week=week,medium=medium ,date=datetime.today())
            Student.save()
            messages.success(request,'Your account has been created.You will be emailed as soon as the teacher is avaliable')
            return render(request,'index.html',locals())
    return render(request,'student_sign.html',locals())

#from somewhere import handle_uploaded_file

##def upload_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            handle_uploaded_file(request.FILES['file'])
#            return HttpResponseRedirect('/success/url/')
#    else:
#        form = UploadFileForm()
#    return render(request, 'upload.html', {'form': form})
