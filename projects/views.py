from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Profile, Project, Rates
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
# Create your views here.
def index(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request,'index.html',{"projects":projects,"profile":profile})


#search view function
@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        project = request.GET.get("project")
        results = Project.search_project(project)
        message = f'project'
        return render(request, 'search.html', {'projects': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

    