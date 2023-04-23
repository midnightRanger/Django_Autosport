from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения Racing")

def competitions(request):
    return HttpResponse("Страница Competition")