from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse คือ ฟังก์ชั่นสำหรับทำให้โชว์ข้อความหน้าเว็บได้

def Home(request):
    return HttpResponse('hello hong')
