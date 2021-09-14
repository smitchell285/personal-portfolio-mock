from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request,'portfolio/projects.html', {'projects':projects})

def Home(request):
    return render(request,'portfolio/home.html')
