# Generated by Django 3.1.12 on 2022-05-17 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_me', models.DateTimeField(auto_now=True)),
                ('image_theme', models.ImageField(default='default.jpg', upload_to='kurs_images')),
                ('creators', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=200, null=True)),
                ('photo', models.ImageField(default='cat_images/default.jpg', upload_to='cat_images')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=30)),
                ('video_id', models.CharField(max_length=11)),
                ('position', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.group'),
        ),
    ]