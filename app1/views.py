from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return HttpResponse('<h1>my first view in APP1</h1>')

def app1_second(request):
    return HttpResponse('<h1><marquee>my second views in APP1</marquee></h1>')