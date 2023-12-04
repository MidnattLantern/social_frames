from django.shortcuts import render, get_object_or_404
from .models import ProjectItem, EpisodeItem
from .models import SceneItem, SketchItem, SketchItemComment
from .forms import SketchItemComment
from django.views import generic, View

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
    context = {
        'show_sketches': render_sketches,
    }
    return render(request, 'storyboard/sketches_view.html', context)

# test
class AnythingSketch(generic.ListView):
    sketch_item = SketchItem
    sketch_item_comment = SketchItemComment
    render_sketch_item = SketchItem.sketch_upload
    render_sketch_item_comment = SketchItemComment.body
    template_name = "index.html"

#def render_scene_view(view):
#    def get(self, request):
#        sketch_item = SketchItem
#        post = get_object_or_404(sketch_item)
#        return render(
#            request,
#            "base.html",
#            {
#                "post": post,
#                "sketch_item_comment": SketchItemComment()
#            }
#        )