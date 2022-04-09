from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('api/projects/', views.ProjectList.as_view()),
    path('',views.index,name='index'),
    
]