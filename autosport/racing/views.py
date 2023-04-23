from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения Racing")

def competitions(request, competition_id):
    if(request.GET):
        print(request.GET)
    if int(competition_id) > 1000:
        return redirect('/racing/')

    return HttpResponse(f"Страница Competition: {competition_id}")

def archive(request, year):
    if int(year) > 2030:
        raise Http404()

    return HttpResponse(f"Year: {year}")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found :( </h1>')