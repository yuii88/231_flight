from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse คือ ฟังก์ชั่นสำหรับทำให้โชว์ข้อความหน้าเว็บได้

def Home(request):
    return render(request,'myapp/home.html')

def Login(request):
    return render(request,'myapp/login.html')
    
def Register(request):
    return render(request,'myapp/register.html')