# This file is created by Tamojit Roy aka 'AstroDestroyer146'

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return HttpResponse("Signup Here")

def signin(request):
    return HttpResponse("Signin Here")

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')