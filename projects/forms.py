from .models import Profile, Project, Rates
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
  # signup form
class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields=('username','full_name','email','password1','password2',)

# updateUserForm
class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields=('username','email',)

# UpdateProfileForm
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['contact','profile_pic', 'bio']         
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile', 'date']

