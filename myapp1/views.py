from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def v1(request):
    return HttpResponse("<h1>This is v1 view from myapp1</h1>")

def v2(request):
    return HttpResponse("<h1>This is v2 view from myapp1</h1>")
