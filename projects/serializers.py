from dataclasses import field
from rest_framework import serializers
from .models import Profile,Project,Moringa
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False,read_only=True)
    class Meta:
        fields=['id','user', 'profile_pic', 'bio', 'contact']
class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Moringa
        fields = ['title','url','description']
      

     