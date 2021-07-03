from django.core.checks import messages
from django.shortcuts import render,redirect
from .models import Faculty,Courses,Contact,Payment
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        information='you have successfully filled the contact form {} and you will get the confirmation email as well'.format(name)
        messages.success(request,information)
        subject='Thank you for your response'
        message='Welcome to StudyAdda {}, We got your mail from {}, we will contact you as soon as possible, Thank You'.format(name,email)
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        

    
    faculties=Faculty.objects.all()
    courses=Courses.objects.all()
    return render(request,'index.html',{'faculties':faculties,'courses':courses})


def payment(request,price,course):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        nameoncard=request.POST.get('nameoncard')
        creditcardnumber=request.POST.get('creditcardnumber')
        cvv=request.POST.get('cvv')
        date=request.POST.get('date')
        Price=request.POST.get('price')
        if int(Price)!=price:
            messages.error(request,'Fill right price what is mentioned in the course')
            return render(request,'index1.html',{'price':price,'course':course})
        payment=Payment(name=name,email=email,nameoncard=nameoncard,creditcardnumber=creditcardnumber,cvv=cvv,date=date,price=Price,courseName=course)
        payment.save()
        subject='Thank you for your response'
        message='Welcome to StudyAdda, we got your response {} from your email {} and we will activate your {} as soon as possible, Thank You'.format(name,email,course)
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,'Your payment form has been successfully filled and confirmation mail has been send')
        return redirect('index')

    return render(request,'index1.html',{'price':price,'course':course})
