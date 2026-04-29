from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.
def mounika(request):
    return HttpResponse("mounika is a student")
def home(request):
    return render(request,'home.html')
def singledata(request):
    object=student.objects.get(id=1)
    return render(request,'singledata.html',{'s':object})
def mul_data(request):
    object=student.objects.all()
    return render(request,'mul_data.html',{'m':object})