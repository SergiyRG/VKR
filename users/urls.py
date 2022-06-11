from django.urls import path

from users.views import Profile, teacher

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('kerkesa/', teacher, name='kerkesa')
]