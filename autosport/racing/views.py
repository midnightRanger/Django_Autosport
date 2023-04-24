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

def get_car(request, id):
    car = Car.objects.filter(id = id)

    if (not car):
        return HttpResponse("Car not found")
    return HttpResponse(car)

def car_index(request):

    car_value = ""

    cars = Car.objects.all()
    if not cars:
        return HttpResponse("There are no cars in DB:(")

    for car in cars:
        car_value += f"{car.pk} - {car.name} \n"
    return HttpResponse(car_value)


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

    ##OR
    ##car = Car.objects.create(name = name, height = height, mass = mass, model = model, mark = mark)

    return HttpResponse(f"Car with id {car.id} was successfully added")



def archive(request, year):
    if int(year) > 2023:
        raise Http404()

    return HttpResponse(f"Year: {year}")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found :( </h1>')