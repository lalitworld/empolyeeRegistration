from django.contrib import admin
from .models import EmployeeDetails,EmployeeEducation,EmployeeExperience
# Register your models here.
admin.site.register([EmployeeDetails,EmployeeEducation,EmployeeExperience])
