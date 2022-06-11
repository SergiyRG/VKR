from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,AboutView,CourseListView, CourseDetailView,LessonDetailView, SearchView, create_group, create_course, create_lesson

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='kerko_kurs'),
    path('krijo/klase', create_group, name='krijo_klase'),
    path('krijo/lende', create_course, name='krijo_lende'),
    path('krijo/mesim', create_lesson, name='krijo_mesim')
]
