from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('lawyerdetail/<str:pk_test>/', views.lawyerdetail, name='lawyer'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
]
