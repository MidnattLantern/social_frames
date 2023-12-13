# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem
# .forms
from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
from .forms import CreateSketchItem, CreateSketchItemComment


""" class based as generic view 
# first thing user sees when they enter Social Frames, expects to see projects
class RenderHomeView(generic.ListView):
    model = ProjectItem
    queryset = ProjectItem.objects.all()
    context_object_name = 'show_projects'
    template_name = 'index.html'

# user enter a project, expects to see episodes
class RenderProjectView(generic.ListView):
    model = EpisodeItem
    template_name = 'project.html'

# user enter an episode, expects to see scenes
class RenderEpisodeView(generic.ListView):
    model = SceneItem
    template_name = 'episode.html'

# user enter a scene, expects to see sketches
class RenderSceneView(generic.ListView):
    model = SketchItem
    template_name = 'scene_view.html'
"""


#    """RenderHomeView"""
# new model
# user enter a project, expects to see episodes
"""
class RenderHomeView(View):
    def get (self, request, *args, **kwargs):
        queryset = ProjectItem.objects.all()
        post = get_object_or_404(queryset)
        return render(
            request,
            'index.html',
            {
                'project_views': post,
#                'create_project_item': CreateProjectItem(),
            },
        )
"""
# old model
# first thing user sees when they enter Social Frames, expects to see projects

class RenderHomeView(generic.ListView):
    model = ProjectItem
    queryset = ProjectItem.objects.all()
    template_name = 'index.html'


#    """RenderProjectView"""
# new model
# user enter a project, expects to see episodes
"""
class RenderProjectView(View):
    def get (self, request, project_slug, *args, **kwargs):
        queryset = EpisodeItem.objects.all()
        post = get_object_or_404(queryset)
        return render(
            request,
            'project_view.html',
            {
                'project_views': post,
#                'create_episode_item': CreateEpisodeItem()
            },
        )
"""
# old model
# user enter a project, expects to see episodes

class RenderProjectView(generic.ListView):
    model = EpisodeItem
    queryset = EpisodeItem.objects.all()
    template_name = 'project_view.html'


#    """RenderEpisodeView"""
# new model
# user enter a episode, expects to see sketches
"""
class RenderEpisodeView(View):
    def get (self, request, episode_slug, *args, **kwargs):
        queryset = SketchItem.objects.all()
        post = get_object_or_404(queryset)
        return render(
            request,
            'episode_view.html',
            {
                'episode_views': post,
#                'create_scene_item': CreateSceneItem()
            },
        )
"""
# old model
# user enter an episode, expects to see scenes

class RenderEpisodeView(generic.ListView):
    model = SceneItem
    queryset = SceneItem.objects.all()
    template_name = 'episode_view.html'


#    """RenderSceneView"""
# new model
# user enter a scene, expects to see sketches
"""
class RenderSceneView(View):
    def get (self, request, scene_slug, *args, **kwargs):
        queryset = SceneItem.objects.all()
        post = get_object_or_404(queryset, scene_slug=scene_slug)
        return render(
            request,
            'scene_view.html',
            {
                'post': post,
            },
        )
"""
# old model
# user enter a scene, expects to see sketches

class RenderSceneView(generic.ListView):
    model = SketchItem
    queryset = SketchItem.objects.all()
    template_name = 'scene_view.html'
