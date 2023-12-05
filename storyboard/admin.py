from django.contrib import admin
from .models import ProjectItem, EpisodeItem
from .models import SceneItem, SketchItem


@admin.register(ProjectItem)
class RegisterProject(admin.ModelAdmin):
    prepopulated_fields = {'project_slug': ('project_name',)}


@admin.register(EpisodeItem)
class RegisterEpisode(admin.ModelAdmin):
    prepopulated_fields = {'episode_slug': ('episode_name',)}


@admin.register(SceneItem)
class RegisterScene(admin.ModelAdmin):
    prepopulated_fields = {'scene_slug': ('scene_name',)}


admin.site.register(SketchItem)
