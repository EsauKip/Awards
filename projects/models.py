
from os import name
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    profile_pic = CloudinaryField('images')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def save_profile(self):
        self.save()
            #delete profile method
    def delete_profile(self):
        self.delete()
        #update profile method
    def update_profile(self):
        self.update()

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id=id)
        return profile
    @classmethod

    def search_profile(cls,search_term):
        profile = cls.objects.filter(name__icontains=search_term)
        return profile


class Project(models.Model):
    title = models.CharField(max_length=100)
    url=models.URLField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('images')
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    def update_project(self):
        self.update()
    @classmethod
    def get_project(cls,id):
        project = cls.objects.get(id=id)
        return project
    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(title__icontains=name).all()
        return project

