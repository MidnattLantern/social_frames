# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem
# .forms (for later use)
#from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
#from .forms import CreateSketchItem, CreateSketchItemComment


#outdated
#def render_sign_in(request):
#    return render(request, 'storyboard/sign_in.html')

#outdated
#def render_sign_out(request):
#    return render(request, 'storyboard/sign_out.html')

#outdated
#def render_sign_up(request):
#    return render(request, 'storyboard/sign_up.html')


""" function based (attempt to transfer to class based)
# first thing user sees when they enter Social Frames, expects to see projects
def render_home_view(request):
    render_project = ProjectItem.objects.all()
    context = {
        'show_projects': render_project,
    }
    return render(request, 'index.html', context)


# user enter a project, expects to see episodes
def render_project_view(request):
    render_episode = EpisodeItem.objects.all()
    context = {
        'show_episodes': render_episode,
    }
    return render(request, 'project_view.html', context)


# user enter an episode, expects to see scenes
def render_episode_view(request):
    render_scene = SceneItem.objects.all()
    context = {
        'show_scenes': render_scene,
    }
    return render(request, 'episode_view.html', context)


# user enter a scene, expects to see sketches
def render_scene_view(request):
    render_sketches = SketchItem.objects.all()
    context = {
        'show_sketches': render_sketches,
    }
    return render(request, 'scene_view.html', context)
"""


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

# first thing user sees when they enter Social Frames, expects to see projects
class RenderHomeView(generic.ListView):
    model = ProjectItem
    queryset = ProjectItem.objects.all()
    template_name = 'index.html'

# new model
# user enter a project, expects to see episodes
class RenderProjectView(View):
    def get (self, request, project_slug, *args, **kwargs):
        queryset = EpisodeItem.objects.all()
        post = get_object_or_404(queryset)
        return render(
            request,
            'project_view.html',
            {
                'post': post,
            },
        )


# old model
# user enter a project, expects to see episodes
"""
class RenderProjectView(generic.ListView):
    model = ProjectItem
    queryset = EpisodeItem.objects.all()
    context_object_name = 'show_episodes'
    template_name = 'project_view.html'
"""
 
# user enter an episode, expects to see scenes
class RenderEpisodeView(View):
    def get (self, request, episode_slug, *args, **kwargs):
        return render(
            request,
            'episode_view.html',
        )

# user enter a scene, expects to see sketches
class RenderSceneView(View):
    def get (self, request, scene_slug, *args, **kwargs):
        return render(
            request,
            'scene_view.html',
        )

