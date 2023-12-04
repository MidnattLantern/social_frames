""" docstring """
from django import forms
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem, SketchItemComment


""" DRY template:
class Create<name>(forms.ModelForm):
    class Meta:
        model: <name>
        fields = ()
"""


class CreateProjectItem(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model: ProjectItem
        fields = ('project_name',)


class CreateEpisodeItem(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model = EpisodeItem
        fields = ('episode_name',)


class CreateSceneItem(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model: SceneItem
        fields = ('scene_name',)


class CreateSketchItem(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model: SketchItem
        fields = ('sketch_upload',)


class CreateSketchItemComment(forms.ModelForm):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model = SketchItemComment
        fields = ('body',)

