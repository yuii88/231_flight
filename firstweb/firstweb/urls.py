"""firstweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
# include คือ คำสั่งการลิ้งค์project กับ myapp ให้เข้ากัน
# path คือ การทำให้เว็บไซต์มี url ย่อย
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')), #ทำให้project ลิ้งค์กับ urls ของเรา

]
