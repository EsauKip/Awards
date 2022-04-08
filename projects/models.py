
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
        
    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id=id)
        return profile
    @classmethod

    def search_profile(cls,search_term):
        profile = cls.objects.filter(name__icontains=search_term)
        return profile

   