
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'fuzzyexpert'

urlpatterns = [
    path('main_form/', views.index, name='covid_main'),
    path('main_form/res', views.result, name='result'),
    path('main_form/c19',views.c19,name='covid19')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
