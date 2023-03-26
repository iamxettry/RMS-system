from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'pages/index.html')

def MenuPage(request):
    return render(request,'pages/menu.html')

def BlogPage(request):
    return render(request,'pages/blog.html')

def EventsPage(request):
    return render(request,'pages/events.html')


def AboutPage(request):
    return render(request,'pages/about.html')

def ContactPage(request):
    return render(request,'pages/contact.html')

