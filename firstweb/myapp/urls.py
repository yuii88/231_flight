#urls.py
from django.urls import path, include 
from .views import * # .views จากไฟล์ที่อยู่ในโฟรเดอร์เดียวกัน

urlpatterns = [
    path('',Home,name='home-page'),
    path('login/',Login,name='login-page'),
    path('register/',Register,name='register-page'),

]