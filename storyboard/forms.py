from .models import SketchItemComment
from django import forms

# generic setup for user interaction, such as comment or sketch submittion, previously named CommentForm()
class WriteSketchComment(forms.ModelForm):
    class Meta:
        model = SketchItemComment
        fields = ('body',)
