from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.
def mounika(request):
    return HttpResponse("mounika is a student")
def home(request):
    return render(request,'home.html')
def singledata(request,id):
    object=student.objects.get(id=id)
    return render(request,'singledata.html',{'s':object})
def mul_data(request):
    object=student.objects.all()
    return render(request,'mul_data.html',{'m':object})
def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        subject=request.POST.get('subject')
    return render(request,'forms.html')

    