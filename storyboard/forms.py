""" docstring """
from django import forms
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem


class CreateProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name',]
        labels = {'project_name': 'Project name',
                  }
    # placeholder for Django (repeating for all objects)
    def __init__(self, *args, **kwargs):
        super(CreateProjectItem, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs['placeholder'] = 'Max 50 characters'
# Edit project item
class EditProjectItem(forms.ModelForm):
    class Meta:
        model = ProjectItem
        fields = ['project_name',]
        labels = {'project_name': 'Project Name'
                  }
    # placeholder for Django (repeating for all objects)
    def __init__(self, *args, **kwargs):
        super(EditProjectItem, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs['placeholder'] = 'Max 50 characters'


class CreateEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_chronology',]
        labels = {'episode_name': 'Episode name',
                  'episode_chronology': 'Chronology',
                  }
    def __init__(self, *args, **kwargs):
        super(CreateEpisodeItem, self).__init__(*args, **kwargs)
        self.fields['episode_name'].widget.attrs['placeholder'] = 'Max 50 characters'
        self.fields['episode_chronology'].widget.attrs['placeholder'] = '___'
# Edit episode item
class EditEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ['episode_name', 'episode_chronology',]
        labels = {'episode_name': 'Episode name',
                  'episode_chronology': 'Chronology'
                  }
    def __init__(self, *args, **kwargs):
        super(EditEpisodeItem, self).__init__(*args, **kwargs)
        self.fields['episode_name'].widget.attrs['placeholder'] = 'Max 50 characters'
        self.fields['episode_chronology'].widget.attrs['placeholder'] = '___'


class CreateSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_chronology', 'scene_event_notes',]
        labels = {'scene_name': 'Scene name',
                  'scene_chronology': 'Chronology',
                  'scene_event_notes': 'Scene event notes'
                  }
    def __init__(self, *args, **kwargs):
        super(CreateSceneItem, self).__init__(*args, **kwargs)
        self.fields['scene_name'].widget.attrs['placeholder'] = 'Max 50 characters'
        self.fields['scene_chronology'].widget.attrs['placeholder'] = '___'
        self.fields['scene_event_notes'].widget.attrs['placeholder'] = 'Max 300 characters'
# Edit scene item
class EditSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ['scene_name', 'scene_chronology', 'scene_event_notes',]
        labels = {'scene_name': 'Scene name',
                  'scene_chronology': 'Chronology',
                  'scene_event_notes': 'Scene event notes'
                  }
    def __init__(self, *args, **kwargs):
        super(EditSceneItem, self).__init__(*args, **kwargs)
        self.fields['scene_name'].widget.attrs['placeholder'] = 'Max 50 characters'
        self.fields['scene_chronology'].widget.attrs['placeholder'] = '___'
        self.fields['scene_event_notes'].widget.attrs['placeholder'] = 'Max 300 characters'


class CreateSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name', 'sketch_image', 'sketch_artist',]
        labels = {'sketch_name': 'Sketch name',
                  'sketch_image': 'JPG or PNG (max 1MB)',
                  'sketch_artist': 'Artist',
                  }
    def __init__(self, *args, **kwargs):
        super(CreateSketchItem, self).__init__(*args, **kwargs)
        self.fields['sketch_name'].widget.attrs['placeholder'] = 'Max 50 characters'
        self.fields['sketch_artist'].widget.attrs['placeholder'] = 'Max 50 characters'
# Edit sketch item
class EditSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_name',]
        labels = {'sketch_name': 'Edit sketch name',
                  }
    def __init__(self, *args, **kwargs):
        super(EditSketchItem, self).__init__(*args, **kwargs)
        self.fields['sketch_name'].widget.attrs['placeholder'] = 'Max 50 characters'
# Edit sketch item
class CommentSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ['sketch_directors_comment',]
        labels = {'sketch_directors_comment': 'Comment',
                  }
    def __init__(self, *args, **kwargs):
        super(CommentSketchItem, self).__init__(*args, **kwargs)
        self.fields['sketch_directors_comment'].widget.attrs['placeholder'] = 'Max 300 characters'
