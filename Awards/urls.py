from django.contrib import admin
from django.urls import re_path,include
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path('admin/', admin.site.urls),
    re_path(r'',include('projects.urls')),
    
    re_path(r'^api-token-auth/', obtain_auth_token)




]