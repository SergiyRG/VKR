import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from courses.models import Group,Course,Lesson
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GroupForm, CourseForm,LessonForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Group.objects.all()
        context['category'] = category
        return context

class AboutView(TemplateView):
    template_name = 'about.html'



def CourseListView(request, category):
    courses = Course.objects.filter(group=category)
    context = {
        'courses':courses
    }
    return render(request, 'courses/course_list.html', context)



class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    model = Course


 
class LessonDetailView(View,LoginRequiredMixin):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'lesson': lesson}
        return render(request, "courses/lesson_detail.html", context)


@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        results = Lesson.objects.filter(title__contains=kerko)
        context = {
            'results':results
        }
        return render(request, 'courses/search_result.html', context)


@login_required
def create_group(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Ваша учетная запись не имеет доступа к этому URL-адресу, только учетные записи учителей!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = GroupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш класс был создан.')
            return redirect('courses:home')
    else:
        form = GroupForm()
    context = {
        'form':form
    }
    return render(request, 'courses/krijo_klase.html', context)


@login_required
def create_course(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Ваша учетная запись не имеет доступа к этому URL адресу, только учетные записи учителей!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            group = form.cleaned_data['group']
            slug = group.id
            messages.success(request, f'Ваша тема создана.')
            return redirect('/courses/' + str(slug))
    else:
        form = CourseForm(initial={'creators':request.user.id, 'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/krijo_lende.html', context)


@login_required
def create_lesson(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Ваша учетная запись не имеет доступа к этому URL адресу только учетные записи учителей!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['course']
            slug = course.slug
            messages.success(request, f'Ваш урок был создан.')
            return redirect('/courses/' + str(slug) )
    else:
        form = LessonForm(initial={'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/krijo_mesim.html', context)


def view_404(request, exception):
    return render(request, '404.html')

def view_403(request, exception):
    return render(request, '403.html')

def view_500(request):
    return render(request, '500.html')