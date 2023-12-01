from .models import SketchItemComment
from django import forms

# generic setup for user interaction, such as comment or sketch submittion, consider renaming CommentForm()
class CommentForm(forms.ModelForm):
    class Meta:
        model = SketchItemComment
        fields = ('comment',)
