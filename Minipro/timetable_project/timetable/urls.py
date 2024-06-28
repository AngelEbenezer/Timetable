from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_timetable, name='generate_timetable'),
    path('api/timetables/', views.api_timetables, name='api_timetables'),
]
