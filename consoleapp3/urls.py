from django.urls import path
from . import views

app_name = 'consoleapp3'

urlpatterns = [
    path('consoleapp/', views.start, name="start" ),
    path('consoleapp/about', views.about, name="about" )
]