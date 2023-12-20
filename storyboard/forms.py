""" docstring """
from django import forms
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem


class CreateProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name', 'project_slug',]
        labels = {'project_name': 'Project name',
                  'project_slug': 'Link name',
                  }


class CreateEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_slug', 'episode_chronology',]
        labels = {'episode_name': 'Episode name',
                  'episode_slug': 'Link name',
                  'episode_chronology': 'Chronology',
                  }


class CreateSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_slug', 'scene_chronology', 'scene_event_notes',]
        labels = {'scene_name': 'Scene name',
                  'scene_slug': 'Link name',
                  'scene_chronology': 'Chronology',
                  'scene_event_notes': 'Scene event notes'
                  }


class CreateSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name', 'sketch_slug', 'sketch_image', 'sketch_artist',]
        labels = {'sketch_name': 'Sketch name',
                  'sketch_slug': 'Link name',
                  'sketch_image': 'JPG/ PNG',
                  'sketch_artist': 'Artist',
                  }



class CreateSketchItemComment(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_directors_comment',]
