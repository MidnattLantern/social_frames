# Generated by Django 3.2.23 on 2023-12-06 01:26

import cloudinary.models
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
            name='EpisodeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_chronology', models.IntegerField()),
                ('episode_name', models.CharField(default='', max_length=50)),
                ('episode_slug', models.SlugField(default='', unique=True)),
                ('episode_creation_date', models.DateTimeField(auto_now_add=True)),
                ('episode_updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['episode_chronology'],
            },
        ),
        migrations.CreateModel(
            name='SketchItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sketch_creation_date', models.DateTimeField(auto_now_add=True)),
                ('sketch_updated_date', models.DateTimeField(auto_now=True)),
                ('sketch_directors_comment', models.CharField(default='', max_length=300)),
            ],
            options={
                'ordering': ['sketch_updated_date'],
            },
        ),
        migrations.CreateModel(
            name='SceneItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_chronology', models.IntegerField()),
                ('scene_name', models.CharField(default='', max_length=50)),
                ('scene_slug', models.SlugField(default='', unique=True)),
                ('scene_creation_date', models.DateTimeField(auto_now_add=True)),
                ('scene_updated_date', models.DateTimeField(auto_now=True)),
                ('scene_event_notes', models.TextField(blank=True, max_length=300, null=True)),
                ('scene_artist_assignment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('scene_property_to_episode', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='storyboard.episodeitem')),
            ],
            options={
                'ordering': ['scene_chronology'],
            },
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50, unique=True)),
                ('project_slug', models.SlugField(default='', unique=True)),
                ('project_poster', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('project_artist_team', models.CharField(max_length=300)),
                ('project_creation_date', models.DateTimeField(auto_now_add=True)),
                ('project_updated_date', models.DateTimeField(auto_now=True)),
                ('project_property_to_director', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['project_updated_date'],
            },
        ),
        migrations.AddField(
            model_name='episodeitem',
            name='episode_property_to_project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='storyboard.projectitem'),
        ),
    ]
