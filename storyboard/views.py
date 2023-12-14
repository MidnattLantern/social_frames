# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem
# .forms
from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
from .forms import CreateSketchItem, CreateSketchItemComment
# authentication to lock out wrong users
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

# generic model
# first thing user sees when they enter Social Frames, expects to see projects
"""
class RenderHomeView(generic.ListView):
    model = ProjectItem
    queryset = ProjectItem.objects.all()
    template_name = 'index.html'
"""

# generic model
# user enter a project, expects to see episodes
"""
class RenderProjectView(generic.ListView):
    model = EpisodeItem
    queryset = EpisodeItem.objects.all()
    template_name = 'project_view.html'
"""

# generic model
# user enter an episode, expects to see scenes
"""
class RenderEpisodeView(generic.ListView):
    model = SceneItem
    queryset = SceneItem.objects.all()
    template_name = 'episode_view.html'
"""

# generic model
# user enter a scene, expects to see sketches
"""
class RenderSceneView(generic.ListView):
    model = SketchItem
    queryset = SketchItem.objects.all()
    template_name = 'scene_view.html'
"""

#   """ Home view """
# non-filter
# user enter a project, expects to see episodes
"""
class RenderHomeView(View):
    def get (self, request, *args, **kwargs):
        project_item = ProjectItem.objects.all()
        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
            },
        )
"""
# filtered
# user enter a project, expects to see episodes
@method_decorator(login_required, name='dispatch')
class RenderHomeView(View):
    def get (self, request, *args, **kwargs):
        project_item = ProjectItem.objects.filter(project_property_to_director=request.user)
        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
            },
        )



#   """ Project view """
# non-filter
# user enter a project, expects to see episodes
"""
class RenderProjectView(View):
    def get (self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(ProjectItem, project_slug=project_slug)
        episode_item = EpisodeItem.objects.all()
        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
            },
        )
"""
# filtered
# user enter a project, expects to see episodes
@method_decorator(login_required, name='dispatch')
class RenderProjectView(View):
    def get (self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(ProjectItem, project_slug=project_slug, project_property_to_director=request.user)
        episode_item = EpisodeItem.objects.filter(episode_property_to_project=project_item)
        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
            },
        )


#   """ Episode view """
# non-filter
# user enter a episode, expects to see sketches
class RenderEpisodeView(View):
    def get (self, request, episode_slug, *args, **kwargs):
        episode_item = get_object_or_404(EpisodeItem, episode_slug=episode_slug)
        scene_item = SceneItem.objects.all()
        return render(
            request,
            'episode_view.html',
            {
                'episode_item': episode_item,
                'scene_item': scene_item,
                
            },
        )


#   """ Scene view """
# non-filter
# user enter a scene, expects to see sketches
class RenderSceneView(View):
    def get (self, request, scene_slug, *args, **kwargs):
        scene_item = get_object_or_404(SceneItem, scene_slug=scene_slug)
        sketch_item = SketchItem.objects.all()
        return render(
            request,
            'scene_view.html',
            {
                'scene_item': scene_item,
                'sketch_item': sketch_item,
            },
        )


