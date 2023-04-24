from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('competition/<int:competition_id>/', competitions),
    path('create_car', create_car),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), ##шаблон с регулярным выражением
]