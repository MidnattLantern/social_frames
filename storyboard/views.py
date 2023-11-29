from django.shortcuts import render
from .models import ProjectItem, EpisodeItem, SceneItem, SketchItem


def render_sign_in(request):
    return render(request, 'storyboard/sign_in.html')


def render_sign_out(request):
    return render(request, 'storyboard/sign_out.html')


def render_sign_up(request):
    return render(request, 'storyboard/sign_up.html')


# first thing user sees when they enter Social Frames, expects to see projects
def render_home(request):
    render_project = ProjectItem.objects.all()
    context = {
        'project': render_project
    }
    return render(request, 'storyboard/home_page.html', context)

"""
def render_project_view(request):
    render_episode = EpisodeItem.objects.all()
    context = {
        'episode': render_episode
    }
    return render(request, 'storyboard/project_view.html', context)
"""

# user enter a project, expects to see episodes

def render_project_view(request):
    render_episode = EpisodeItem.objects.all()
    context = {
        'episode': render_episode
    }
    return render(request, 'storyboard/project_view.html', context)


# user enter an episode, expects to see scenes
def render_episode_view(request):
    render_scene = SceneItem.objects.all()
    context = {
        'scene': render_scene
    }
    return render(request, 'storyboard/episode_view.html', context)


# user enter a scene, expects to see sketches
def render_scene_view(request):
    render_sketches = SketchItem.objects.all()
    context = {
        'sketches': render_sketches
    }
    return render(request, 'storyboard/sketches_view.html', context)