from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('competition/<int:competition_id>/', competitions),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), ##шаблон с регулярным выражением
]