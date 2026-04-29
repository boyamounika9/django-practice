from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mounika(request):
    return HttpResponse("mounika is a student")
def home(request):
    return render(request,'home.html')