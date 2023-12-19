from django.shortcuts import render, HttpResponse
from .models import *

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