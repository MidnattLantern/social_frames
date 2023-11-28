from django.contrib import admin
from .models import ProjectItem, EpisodeItem, SceneItem, SketchItem

admin.site.register(ProjectItem)
admin.site.register(EpisodeItem)
admin.site.register(SceneItem)
admin.site.register(SketchItem)
