from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.IntegerField()
    empdept = models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=50,null=True)
    joindat = models.DateField(null=True)
    
    def __str__(self) -> str:
        return self.user.username
    class Meta:
        db_table =' Employee Table'


class EmployeeEducation(models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pg_course = models.CharField(max_length = 200, null = True)
    pg_clg = models.CharField(max_length = 200, null = True)
    pg_year_of_passing = models.CharField(max_length = 20, null = True)
    pg_percentage = models.CharField(max_length = 20, null = True)
    graduation = models.CharField(max_length = 200, null = True)
    graduation_clg = models.CharField(max_length = 200, null = True)
    graduation_year_of_passing = models.CharField(max_length = 20, null = True)
    graduation_percentage = models.CharField(max_length = 20, null = True)
    hsc = models.CharField(max_length = 200, null = True)
    hsc_clg = models.CharField(max_length = 200, null = True)
    hsc_year_of_passing = models.CharField(max_length = 20, null = True)
    hsc_percentage = models.CharField(max_length = 20, null = True)
    ssc = models.CharField(max_length = 200, null = True)
    ssc_school = models.CharField(max_length = 200, null = True)
    ssc_year_of_passing = models.CharField(max_length = 20, null = True)
    ssc_percentage = models.CharField(max_length = 20, null = True)

    class Meta:
        db_table = "empeducation"

    def __str__(self) :
        return self.User.username

class EmployeeExperience(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    First_company_name = models.CharField(max_length = 200, null = True)
    First_company_desg = models.CharField(max_length = 200, null = True)
    First_company_duration = models.CharField(max_length = 200, null = True)
    First_company_sal = models.CharField(max_length = 200, null = True)
    Second_company_name = models.CharField(max_length = 200, null = True)
    Second_company_desg = models.CharField(max_length = 200, null = True)
    Second_company_duration = models.CharField(max_length = 200, null = True)
    Second_company_sal = models.CharField(max_length = 200, null = True)
    Third_company_name = models.CharField(max_length = 200, null = True)
    Third_company_desg = models.CharField(max_length = 200, null = True)
    Third_company_duration = models.CharField(max_length = 200, null = True)
    Third_company_sal = models.CharField(max_length = 200, null = True)

    class Meta:
        db_table = "empexperience"

    def __str__(self) :
        return self.User.username
    
    