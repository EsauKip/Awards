import profile
from django.shortcuts import render
from .models import Project,Profile
# Create your views here.
def index(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request,'index.html',{"projects":projects,"profile":profile})