from django.db import models
#additional
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# make migration for each edit

PIN = ((0, "not pinned"), (1, "Pinned"))


class ProjectItem(models.Model):
    project_name = models.CharField(max_length=50, null=False, blank=False)
    property_to_director = models.CharField(max_length=50, null=False, blank=False)
    artist_team = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_date']

    def __str__(self):
        return self.project_name


class EpisodeItem(models.Model):
    chronology = models.IntegerField(null=False, blank=False)
    episode_name = models.CharField(max_length=50, null=False, blank=False)
    property_to_project = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['chronology']

    def __str__(self):
        return self.episode_name


class SceneItem(models.Model):
    chronology = models.IntegerField(null=False, blank=False)
    scene_name = models.CharField(max_length=50, null=False, blank=False)
    property_to_episode = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    scene_event_notes = models.TextField(max_length=300, null=True, blank=True)
    artist_assignment = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ['chronology']

    def __str__(self):
        return self.scene_name


class SketchItem(models.Model):
    sketch_upload = CloudinaryField('image', default='placeholder')
    artist = models.CharField(max_length=50, null=False, blank=False)
    property_to_scene = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    pin = models.IntegerField(choices=PIN, default=False)

    class Meta:
        ordering = ['updated_date']

    def __str__(self):
        return self.property_to_scene
