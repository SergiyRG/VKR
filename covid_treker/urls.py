from django.urls import path
from . import views

app_name = 'covid_treker'

urlpatterns = [
    path('statistic/', views.statistic, name="statistic" )
]