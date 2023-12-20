from django.shortcuts import render, HttpResponse
from .models import *

from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def team(request):
    lawyer = Lawyer.objects.all()
    context = {'lawyer':lawyer}
    return render(request, 'home/team.html', context)

def lawyerdetail(request, pk_test):
    lawyer = Lawyer.objects.get(id=pk_test)
    context = {'lawyer':lawyer}
    return render(request, 'home/lawyerdetail.html', context)

def services(request):
    return render(request, 'home/services.html')


def aboutus(request):
    return render(request, 'home/aboutus.html')


def contactus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f"Contact Form Submission from {name}",
                f"Name: {name}\nPhone Number: {phone_number}\nEmail: {email}\nMessage:{message}",
                "sardarhamza538@gmail.com",
                ["hamzaarif1807@gmail.com"],
                fail_silently=False,
            )
            return render(request, 'home/contactus.html', {'form':form, 'success':True})
    else:
        form = ContactForm()


    return render(request, 'home/contactus.html', {'form':form, 'success':False})