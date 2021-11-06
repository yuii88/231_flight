#urls.py
from django.urls import path, include 
from .views import Home # .views จากไฟล์ที่อยู่ในโฟรเดอร์เดียวกัน

urlpatterns = [
    path('',Home),

]