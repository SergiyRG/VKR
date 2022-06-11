from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Group(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length= 200, null=True)
    photo = models.ImageField(upload_to='media/cat_images', default='media/default.png')

    def __str__(self):
        return '{}'.format(self.title)

class Course(models.Model):
    creators = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_me = models.DateTimeField(auto_now=True)
    image_theme = models.ImageField(upload_to='media/kurs_images', default='media/default.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.course.slug,'lesson_slug':self.slug})