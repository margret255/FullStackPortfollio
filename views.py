from django.shortcuts import render

# Create your views here.

def Home(request)
  return render(request,"index.html")


def about(request)
  return render(request,"about.html")
              
def projects(requeat)
  return render(request,"projects.html")


def contact(request)
  return render(request,"contact.html")
