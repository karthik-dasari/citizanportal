from django.urls import path

from .views import *

urlpatterns = [
    path('',login, name='login'),
    path('login/',login, name='login'),
    
    path('register/',register, name='register'),
    
    path('logout/',logout, name='logout'),
    
    path('home/',home, name='home'),
    path('category/',category, name='category'),
    
    path('getlocation/',getlocation, name='getlocation'),
    
    path('dashboard/',dashboard, name='dashboard'),
    path('policedashboard/',policedashboard, name='policedashboard')
]
