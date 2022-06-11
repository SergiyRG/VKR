from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'fuzzyexpert2'

urlpatterns = [
    path('study_form/', views.index, name='study_form'),
    path('study_form/conclusion', views.result, name='conclusion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
