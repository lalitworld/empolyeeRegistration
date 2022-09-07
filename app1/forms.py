from django import forms
from .models import EmployeeDetails

class ProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['empcode','empdept','designation','address','gender','joindat']
        