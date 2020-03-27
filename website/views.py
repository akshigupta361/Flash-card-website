from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def add(request):
    return render(request, 'add.html', {})

def subtract(request):
    return render(request, 'subtract.html', {})

def multiply(request):
    return render(request, 'multiply.html', {})

def divide(request):
    return render(request, 'divide.html', {})