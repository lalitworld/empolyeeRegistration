import profile
import re
from django.shortcuts import render,redirect
# Create your views here.
from .models import EmployeeDetails
from django.contrib.auth.models import User
from django.http import HttpResponse
from app1.forms import ProfileForm
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
            firstname =request.POST['first_name']
            lastname =request.POST['last_name']
            Email =request.POST['email']
            password = request.POST['pwd']
            Empid = request.POST['empid']
            User_obj = User.objects.create_user(first_name = firstname,
                                    last_name = lastname,
                                    username = Email,
                                    password = password)
            Emp_obj = EmployeeDetails.objects.create(user =User_obj,empcode=Empid)    
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
       
    return render(request,'emplogin.html')

def emp_home(request):
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
