""" docstring """
from django import forms
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem


class CreateProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name', 'project_slug',]
        labels = {'project_name': 'Project name',
                  'project_slug': 'Link name (no spaces)',
                  }
# Edit project item
class EditProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name',]
        labels = {'project_name': 'project_name'
                  }


class CreateEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_slug', 'episode_chronology',]
        labels = {'episode_name': 'Episode name',
                  'episode_slug': 'Link name (no spaces)',
                  'episode_chronology': 'Chronology',
                  }
# Edit episode item
class EditEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_chronology',]
        labels = {'episode_name': 'Episode name',
                  'episode_chronology': 'Chronology'
                  }


class CreateSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_slug', 'scene_chronology', 'scene_event_notes',]
        labels = {'scene_name': 'Scene name',
                  'scene_slug': 'Link name (no spaces)',
                  'scene_chronology': 'Chronology',
                  'scene_event_notes': 'Scene event notes'
                  }
# Edit scene item
class EditSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_chronology', 'scene_event_notes',]
        labels = {'scene_name': 'Scene name',
                  'scene_chronology': 'Chronology',
                  'scene_event_notes': 'Scene event notes'
                  }


class CreateSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name', 'sketch_slug', 'sketch_image', 'sketch_artist',]
        labels = {'sketch_name': 'Sketch name',
                  'sketch_slug': 'Link name (no spaces)',
                  'sketch_image': 'JPG/ PNG (max 3MB)',
                  'sketch_artist': 'Artist',
                  }
# Edit sketch item
class EditSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name',]
        labels = {'sketch_name': 'Edit sketch name',
                  }
# Edit sketch item
class CommentSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_directors_comment',]
        labels = {'sketch_directors_comment': 'Comment',
                  }
