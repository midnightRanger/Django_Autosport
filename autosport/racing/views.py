from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from racing.models import Car


def index(request):
    return HttpResponse("Страница приложения Racing")

def competitions(request, competition_id):
    if(request.GET):
        print(request.GET)
    if int(competition_id) > 1000:
        return redirect('home')

    return HttpResponse(f"Страница Competition: {competition_id}")

def create_car(request):
    if not request.GET:
        return Http404()

    name = request.GET.get("name", "Undefined")
    height = request.GET.get("height", 1.0)
    mass = request.GET.get("mass", 1.0)
    model = request.GET.get("model", "Undefined")
    mark = request.GET.get("mark", "Undefined")

    car = Car(name = name, height = height, mass = mass, model = model, mark = mark)
    car.save()



def archive(request, year):
    if int(year) > 2023:
        raise Http404()

    return HttpResponse(f"Year: {year}")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found :( </h1>')