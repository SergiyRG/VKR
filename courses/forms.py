from django import forms
from django.contrib.auth.models import User
from .models import Group, Course, Lesson

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        help_texts = {
            'title': 'Например: Группа 09-851 или ИВМиИТ',
            'description':'Добавьте краткое описание',
            'photo':'Вы можете поместить фотографию или оставить ее пустой'
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['creators','slug', 'title', 'group', 'description', 'image_theme']
        help_texts = {
            'title': 'Например: Основы Prolog, Создаём игру на Prolog и т.д',
            'description':'Краткое содержание',
            'group':'Выберите группу, для которой вы будете создавать курс',
            'image_theme':'Вы можете поместить изображение или оставить его пустым'
        }
        labels = {
            'title':'Topic name'
        }
        widgets = {'creators': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'course', 'video_id', 'position' ]
        help_texts = {
            'title':'Введите название занятия',
            'course':'Выберите курс, к которому это занятие относится',
            'video_id':'Установите ID для видео на Youtube,которое хотите загрузить.(<a href="/media/youtube_help.png">Где я могу найти ID?</a>)',
            'position':'Введите номер позиции или порядок проведения занятия'
        }
        widgets = {
            'slug': forms.HiddenInput()
        }