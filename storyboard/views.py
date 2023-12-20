# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem
# .forms
from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
from .forms import CreateSketchItem



import cloudinary.uploader
# authentication to lock out wrong users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


# user enter a project, expects to see episodes
# request.USER for all
@method_decorator(login_required, name='dispatch')
class RenderHomeView(View, LoginRequiredMixin):
    def get (self, request, *args, **kwargs):
        project_item = ProjectItem.objects.filter(project_property_to_director=request.user)
        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
                'create_project_item': CreateProjectItem(),
            },
        )
    def post (self, request, *args, **kwargs):
        project_item = ProjectItem.objects.filter(project_property_to_director=request.user)
        project_item_form = CreateProjectItem(data=request.POST)
        if project_item_form.is_valid():
            project = project_item_form.save(commit=False)
            project.project_property_to_director = request.user
            project.post = project_item
            project.save()
        else:
            project_item_form = CreateProjectItem()
        if 'delete_project' in request.POST:
            delete_project_slug = request.POST.get('delete_project')
            delete_project = ProjectItem.objects.get(project_slug=delete_project_slug)
            delete_project.delete()
        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
                'create_project_item': CreateProjectItem(),
            },
        )         


# user enter a project, expects to see episodes
@method_decorator(login_required, name='dispatch')
class RenderProjectView(View, LoginRequiredMixin):
    def get (self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(ProjectItem, project_slug=project_slug)
        #users with access to link can't access to other teams episode(s)
        episode_item = EpisodeItem.objects.filter(episode_property_to_project=project_item, episode_property_to_director=request.user)
        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
                'create_episode_item': CreateEpisodeItem(),
            },
        )
    def post (self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(ProjectItem, project_slug=project_slug)
        #users with access to link can't access to other teams episode(s)
        episode_item = EpisodeItem.objects.filter(episode_property_to_project=project_item, episode_property_to_director=request.user)
        episode_item_form = CreateEpisodeItem(data=request.POST)
        if episode_item_form.is_valid():
            episode = episode_item_form.save(commit=False)
            episode.episode_property_to_project = project_item
            episode.episode_property_to_director = request.user
            episode.post = episode_item
            episode.save()
        else:
            episode_item_form = CreateEpisodeItem()
        if 'delete_episode' in request.POST:
            delete_episode_slug = request.POST.get('delete_episode')
            delete_episode = EpisodeItem.objects.get(episode_slug=delete_episode_slug)
            delete_episode.delete()
        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
                'create_episode_item': CreateEpisodeItem(),
            },
        )


# user enter a episode, expects to see scenes
@method_decorator(login_required, name='dispatch')
class RenderEpisodeView(View, LoginRequiredMixin):
    def get (self, request, episode_slug, *args, **kwargs):
        episode_item = get_object_or_404(EpisodeItem, episode_slug=episode_slug)
        scene_item = SceneItem.objects.filter(scene_property_to_episode=episode_item)
        return render(
            request,
            'episode_view.html',
            {
                'episode_item': episode_item,
                'scene_item': scene_item,
                'create_scene_item': CreateSceneItem(),
            },
        )
    def post (self, request, episode_slug, *args, **kwargs):
        episode_item = get_object_or_404(EpisodeItem, episode_slug=episode_slug)
        scene_item = SceneItem.objects.filter(scene_property_to_episode=episode_item)
        scene_item_form = CreateSceneItem(data=request.POST)
        if scene_item_form.is_valid():
            scene = scene_item_form.save(commit=False)
            scene.scene_property_to_episode = episode_item
            scene.post = scene_item
            scene.save()
        else:
            scene_item_form = CreateSceneItem()
        if 'delete_scene' in request.POST:
            delete_scene_slug = request.POST.get('delete_scene')
            delete_scene = SceneItem.objects.get(scene_slug=delete_scene_slug)
            delete_scene.delete()
        return render(
            request,
            'episode_view.html',
            {
                'episode_item': episode_item,
                'scene_item': scene_item,
                'create_scene_item': CreateSceneItem(),
            },
        )


# user enter a scene, expects to see sketches
@method_decorator(login_required, name='dispatch')
class RenderSceneView(View, LoginRequiredMixin):
    def get (self, request, scene_slug, *args, **kwargs):
        scene_item = get_object_or_404(SceneItem, scene_slug=scene_slug)
        sketch_item = SketchItem.objects.filter(sketch_property_to_scene=scene_item)
        return render(
            request,
            'scene_view.html',
            {
                'scene_item': scene_item,
                'sketch_item': sketch_item,
                'create_sketch_item': CreateSketchItem(),
            },
        )
    def post (self, request, scene_slug, *args, **kwargs):
        scene_item = get_object_or_404(SceneItem, scene_slug=scene_slug)
        sketch_item = SketchItem.objects.filter(sketch_property_to_scene=scene_item)
        sketch_item_form = CreateSketchItem(request.POST, request.FILES)
        if sketch_item_form.is_valid():
            sketch = sketch_item_form.save(commit=False)
            sketch.sketch_property_to_scene = scene_item
            sketch.post = sketch_item
            sketch.save()
        else:
            sketch_item_form = CreateSketchItem()
        if 'delete_sketch' in request.POST:
            delete_sketch_slug = request.POST.get('delete_sketch')
            delete_sketch = SketchItem.objects.get(sketch_slug=delete_sketch_slug)
            delete_sketch.delete()

        return render(
            request,
            'scene_view.html',
            {
                'scene_item': scene_item,
                'sketch_item': sketch_item,
                'create_sketch_item': CreateSketchItem(),

            },
        )
