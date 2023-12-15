from django.contrib import admin
from .models import ProjectItem, EpisodeItem
from .models import SceneItem, SketchItem

""" naming convention:
Each item related to a function are appended with "admin"
"""


"""
- Different users can make a project each with the same name.
Social Frames/ CloudyBoard tell them apart with an index id assigned to each
user. Hence, `('project_property_to_director', 'project_name',)`.
"""
@admin.register(ProjectItem)
class RegisterProject(admin.ModelAdmin):
    prepopulated_fields = {'project_slug': ('project_property_to_director',
                                            'project_name',
                                            )}


@admin.register(EpisodeItem)
class RegisterEpisode(admin.ModelAdmin):
    prepopulated_fields = {'episode_slug': ('episode_name',)}


@admin.register(SceneItem)
class RegisterScene(admin.ModelAdmin):
    prepopulated_fields = {'scene_slug': ('scene_name',)}


@admin.register(SketchItem)
class RegisterSketch(admin.ModelAdmin):
    prepopulated_fields = {'sketch_slug': ('sketch_name',)}
    actions = ['sketch_pin']

    # followed the tutorial, not sure if this is right
    def pin(self, request, queryset):
        queryset.update(sketch_pin=True)
