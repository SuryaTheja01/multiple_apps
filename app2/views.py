from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_app2(request):
    return HttpResponse('<h1>my first views in APP2</h1>')


def second_app2(request):
    return HttpResponse('<h1><marquee>my second views in APP2</marquee></h1>')