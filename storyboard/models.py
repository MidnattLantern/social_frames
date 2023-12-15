from django.db import models
# additional
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# make migration for each edit

PIN = ((0, "not pinned"), (1, "Pinned"))

""" Naming conventions:
- Each item are appended with "Create" when exported to `forms.py`.
- Each item, such as "project" share similar model names such as `_name`,
appended item name differenciate between exaple: `PROJECT_name` and
`EPISODE_name`.
- The section like folders on Finder/ File Exploer are as following:
Project > Episode > Scene > Sketch.
- `property_to...` reference to the item before. Example: `Episode` belongs to
`Project`, so the name is `EPISODE_property_to_PROJECT`. Exception for Project,
that belongs to a User.
"""


class ProjectItem(models.Model):
    project_name = models.CharField(
        max_length=50, null=False, blank=False, default='', unique=False)
    project_slug = models.SlugField(
        max_length=50, unique=True, default='', null=False)
    project_poster = CloudinaryField(
        'image', default='', blank=True, null=True)
    project_creation_date = models.DateTimeField(
        auto_now_add=True)
    project_updated_date = models.DateTimeField(
        auto_now=True)
    project_property_to_director = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ['project_updated_date']

    def __str__(self):
        return self.project_name


class EpisodeItem(models.Model):
    episode_chronology = models.IntegerField(null=False, blank=False)
    episode_name = models.CharField(
        max_length=50, null=False, blank=False, default='', unique=False)
    episode_slug = models.SlugField(max_length=50, unique=True, default='', null=False)
    episode_property_to_project = models.ForeignKey(
        ProjectItem, on_delete=models.CASCADE, default='', null=True,
        blank=True)
    episode_creation_date = models.DateTimeField(auto_now_add=True)
    episode_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['episode_chronology']

    def __str__(self):
        return self.episode_name


class SceneItem(models.Model):
    scene_chronology = models.IntegerField(null=False, blank=False)
    scene_name = models.CharField(
        max_length=50, null=False, blank=False, default='', unique=False)
    scene_slug = models.SlugField(max_length=50, unique=True, default='', null=False)
    scene_property_to_episode = models.ForeignKey(
        EpisodeItem, on_delete=models.CASCADE, default='')
    scene_creation_date = models.DateTimeField(auto_now_add=True)
    scene_updated_date = models.DateTimeField(auto_now=True)
    scene_event_notes = models.TextField(max_length=300, null=True, blank=True)
    scene_artist_assignment = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ['scene_chronology']

    def __str__(self):
        return self.scene_name


class SketchItem(models.Model):
    sketch_name = models.CharField(
        max_length=50, null=False, blank=False, default='', unique=False)
    sketch_slug = models.SlugField(max_length=50, unique=True, default='', null=False)
    sketch_property_to_scene = models.ForeignKey(
        SceneItem, on_delete=models.CASCADE, default='')
    sketch_creation_date = models.DateTimeField(auto_now_add=True)
    sketch_updated_date = models.DateTimeField(auto_now=True)
    sketch_directors_comment = models.CharField(
        max_length=300, null=True, blank=True, default='')
    sketch_artist = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    sketch_pin = models.BooleanField(default=False)
    sketch_image = CloudinaryField('image', default='')

    class Meta:
        ordering = ['sketch_updated_date']

    def __str__(self):
        return self.sketch_name
