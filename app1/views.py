from django.shortcuts import render
from app1.forms import RegisterForm
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("User created successfully")
    data = RegisterForm
    return render(request,'registration.html',{"form":data})