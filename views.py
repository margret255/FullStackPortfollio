from django.shortcuts import render,redirect
from django.contrib.auth import user authentication
from django.contrib import messages


# Create your views here.

def Home(request)
  return render(request,"index.html")


def about(request)
  return render(request,"about.html")

  
def login(request)
if request.method=="POST"
  username=request.POST["|username"]
  password=request.POST["passqord"]
  user=authenticate(request,user)
if user is  not None:
  login(request,user)
  return redirect(home)
else:
  messages.succcess(requestm("An error ocurred please try again")
  pass

return render(request,"|login.html)
  
              
def projects(requeat)
  return render(request,"projects.html")


def contact(request)
  return render(request,"contact.html")
