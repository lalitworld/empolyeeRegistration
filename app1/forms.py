

from django import forms
from .models import EmployeeDetails,EmployeeEducation

class ProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['empcode','empdept','designation','address','gender','joindat']


# def current_user(request) :
#     user = request.user
#     employee = EmployeeDetails.objects.get(user = user)  
#     return employee.user.firstname     
# class  EmployeeEducationForm(forms.ModelForm):
    
#     # current_user(request)
#     class Meta:
#         model  =EmployeeEducation
#         # fields = '__all__'      
#         exclude = ['user'] 
        