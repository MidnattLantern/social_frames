""" docstring """
from django import forms
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem


""" DRY template:
class Create<name>(forms.ModelForm):
    class Meta:
        model: <name>
        fields = ()
"""


class CreateProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name', 'project_slug', 'project_property_to_director',]


class CreateEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_slug', 'episode_property_to_project', 'episode_chronology',]


class CreateSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_slug', 'scene_property_to_episode', 'scene_chronology', 'scene_artist_assignment',]


class CreateSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name',]


class CreateSketchItemComment(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_directors_comment',]

