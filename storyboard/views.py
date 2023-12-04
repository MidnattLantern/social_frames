# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem, SketchItemComment
# .forms
from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
from .forms import CreateSketchItem, CreateSketchItemComment


#outdated
def render_sign_in(request):
    return render(request, 'storyboard/sign_in.html')

#outdated
def render_sign_out(request):
    return render(request, 'storyboard/sign_out.html')

#outdated
def render_sign_up(request):
    return render(request, 'storyboard/sign_up.html')


# first thing user sees when they enter Social Frames, expects to see projects
def render_home(request):
    render_project = ProjectItem.objects.all()
    context = {
        'show_projects': render_project,
    }
    return render(request, 'storyboard/index.html', context)


# user enter a project, expects to see episodes
def render_project_view(request):
    render_episode = EpisodeItem.objects.all()
    context = {
        'show_episodes': render_episode,
    }
    return render(request, 'storyboard/project_view.html', context)


# user enter an episode, expects to see scenes
def render_episode_view(request):
    render_scene = SceneItem.objects.all()
    context = {
        'show_scenes': render_scene,
    }
    return render(request, 'storyboard/episode_view.html', context)


# user enter a scene, expects to see sketches
def render_scene_view(request):
    render_sketches = SketchItem.objects.all()
    render_sketches_comments = SketchItemComment.objects.all()
    context = {
        'show_sketches': render_sketches,
        'show_sketches_comments': render_sketches_comments,
    }
    return render(request, 'storyboard/sketches_view.html', context)

# appended with "Load"
class LoadProjectItem(generic.ListView):
    project_item = ProjectItem
    render_project_item = ProjectItem.project_name


class LoadEpisodeItem(generic.ListView):
    episode_item = EpisodeItem
    render_episode_item = EpisodeItem.episode_name


class LoadSceneItem(generic.ListView):
    scene_item = SceneItem
    render_scene_item = scene_item.scene_name

class LoadSketchItem(generic.ListView):
    sketch_item = SketchItem
    render_sketch_item = SketchItem.sketch_upload


class LoadSketchItemComment(generic.ListView):
    sketch_item_comment = SketchItemComment
    render_sketch_item_comment = SketchItemComment.body

