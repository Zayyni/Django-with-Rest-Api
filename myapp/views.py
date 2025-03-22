from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v1(request):
    return HttpResponse("<h1>This is v1 view from myapp</h1>")

def v2(request):
    return HttpResponse("<h1>This is v2 view from myapp</h1>")
