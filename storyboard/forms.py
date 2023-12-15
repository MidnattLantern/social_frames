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
        fields = ('project_name',)


class CreateEpisodeItem(forms.ModelForm):
    class Meta:
        model = EpisodeItem
        fields = ('episode_name',)


class CreateSceneItem(forms.ModelForm):
    class Meta:
        model = SceneItem
        fields = ('scene_name',)


class CreateSketchItem(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ('sketch_name',)


class CreateSketchItemComment(forms.ModelForm):
    class Meta:
        model = SketchItem
        fields = ('sketch_directors_comment',)

