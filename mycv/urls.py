from django.urls import path
from .views import cv_maker, resume, list


urlpatterns = [
    path('', cv_maker, name='cv_maker'),
    path('resume/<int:pk>/', resume, name='resume'),
    path('list/', list, name='list'),

]
