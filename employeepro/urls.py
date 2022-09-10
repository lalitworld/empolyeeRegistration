"""employeepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import index,registration,emplogin,emp_home,emp_profile,Logout,education_details,show_education,edit_experiance_details,show_experiance,admin_login,admin_home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registration/',registration,name='registration'),
    path('emplogin/',emplogin,name='emplogin'),
    path('emp-home/',emp_home,name='emp_home'),
    path('emp-profile/',emp_profile,name='emp_profile'),
    path('logout/',Logout,name='logout'),
    path('edit-education/',education_details,name='education_details'),
    path('education/',show_education,name='show_education'),
    path('edit-experiance-details/',edit_experiance_details,name='edit_experiance_details'),
    path('show-experiance/',show_experiance,name='show_experiance'),
    path('admin-login/',admin_login,name='adminlogin'),
    path('admin-home/',admin_home,name='admin_home'),
    
    
            
]
