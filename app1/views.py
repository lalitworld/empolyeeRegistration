import profile
import re
from django.shortcuts import render,redirect
# Create your views here.
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from app1.forms import ProfileForm
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
            print("in post")
            firstname =request.POST['first_name']
            lastname =request.POST['last_name']
            Email =request.POST['email']
            password = request.POST['pwd']
            Empid = request.POST['empid']
            User_obj = User.objects.create_user(first_name = firstname,
                                    last_name = lastname,
                                    username = Email,
                                    password = password)
            EmployeeDetails.objects.create(user =User_obj,empcode=Empid)
            EmployeeEducation.objects.create(user =User_obj)    
            EmployeeExperience.objects.create(user =User_obj)    
                
            return HttpResponse("User created successfully")
    
    return render(request,'registration.html')

def emplogin(request):
    print("before post")
    if request.method == 'POST':
        print("in post")
        Email = request.POST['email']
        password = request.POST['pwd']
        user =authenticate(username=Email,password=password)
        print(user)
        if user:
           login(request, user)
           return redirect('emp_home')
        else:
            return redirect('emplogin')
       
    return render(request,'emplogin.html')

def emp_home(request):
    if not request.user.is_authenticated :
        return redirect("emplogin")
    return render(request,'emp_home.html')

def emp_profile(request) :
    if not request.user.is_authenticated :
        return redirect("emplogin")
    user = request.user
    employee = EmployeeDetails.objects.get(user = user)
    err = ""
    if request.method == "POST":
    
        employee.user.firstname = request.POST["Firstname"]
        employee.user.lastname = request.POST["Lastname"]
        employee.empcode = request.POST["Empcode"]
        employee.email = request.POST["Emailid"]
        employee.designation = request.POST["Designation"]
        employee.empdept = request.POST["Empdept"]
        employee.address = request.POST["address"]
        employee.joindat = request.POST["joindate"]
        employee.save() # to save the changes in the fields which are defined by user
        employee.user.save() # to save the changes in those fields which comes up with dwfault model
        error = "No"
        return redirect('emp_home')        
    return render(request, "profile.html", locals()) # becausee of locals() we don't need to pass context it will take all the variables

def Logout(request):
    logout(request)
    return redirect('index')


def education_details(request):
    user = request.user
    edu = EmployeeEducation.objects.get(user = user)
    if request.method == 'POST':
        edu.pg_course = request.POST["pgcourse"]
        edu.pg_clg = request.POST["pgclg"]
        edu.pg_year_of_passing = request.POST["pg_year_of_passing"]
        edu.pg_percentage = request.POST["pg_percentage"]
        edu.graduation = request.POST["gcourse"]
        edu.graduation_clg = request.POST["gclg"]
        edu.graduation_year_of_passing = request.POST["g_year_of_passing"]
        edu.graduation_percentage = request.POST["g_percentage"]
        edu.hsc = request.POST["hsc"] 
        edu.hsc_clg = request.POST["hscclg"]
        edu.hsc_year_of_passing = request.POST["hsc_year_of_passing"]
        edu.hsc_percentage = request.POST["hsc_percentage"]
        edu.ssc = request.POST["ssc"]
        edu.ssc_school = request.POST["sscschool"]
        edu.ssc_year_of_passing = request.POST["ssc_year_of_passing"]
        edu.ssc_percentage = request.POST["ssc_percentage"]
        edu.save()
        return redirect('emp_home')
           # print(request.body)

    return render(request,'education.html',locals())

def show_education(request):
    user = request.user
    edu = EmployeeEducation.objects.get(user = user)
    return render(request,'education_show.html',locals())




def edit_experiance_details(request):
    user = request.user
    edu = EmployeeExperience.objects.get(user = user)
    if request.method == 'POST':
        edu.First_company_name = request.POST["First_company_name"]
        edu.First_company_desg = request.POST["First_company_desg"]
        edu.First_company_duration = request.POST["First_company_duration"]
        edu.First_company_sal = request.POST["First_company_sal"]
        edu.Second_company_name = request.POST["Second_company_name"]
        edu.Second_company_desg = request.POST["Second_company_desg"]
        edu.Second_company_duration = request.POST["Second_company_duration"]
        edu.Second_company_sal = request.POST["Second_company_sal"]
        edu.Third_company_name = request.POST["Third_company_name"] 
        edu.Third_company_desg = request.POST["Third_company_desg"]
        edu.Third_company_duration = request.POST["Third_company_duration"]
        edu.Third_company_sal = request.POST["Third_company_sal"]
        
        edu.save()
        return redirect('emp_home')
           # print(request.body)

    return render(request,'edit_experiance.html',locals())

def show_experiance(request):
    user = request.user
    edu = EmployeeExperience.objects.get(user = user)
    return render(request,'experiance_show.html',locals())



def admin_login(request) :
    err_msg = ""
    if request.method == "POST" :
        u = request.POST["email"]
        p = request.POST["pwd"]
        user = authenticate(username = u, password = p)
        
        if request.user.is_superuser: # for superuser is_staff status has to be True if its not True then it will not be superuser
            login(request, user)
            err_msg = "No"
            return HttpResponse("login as superuser")
        return redirect('adminlogin')
            
    return render(request, "admin_login.html", locals())


def admin_home(request) :
    if not request.user.is_authenticated :
        return render(request, "admin_login.html")
    if  request.user.is_superuser:
        return redirect("admin_home")
    return redirect('index')