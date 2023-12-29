# 3rd party
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import UpdateView
# .models
from .models import ProjectItem, EpisodeItem, SceneItem
from .models import SketchItem
# .forms that create new objects
from .forms import CreateProjectItem, CreateEpisodeItem, CreateSceneItem
from .forms import CreateSketchItem

# .forms that edit existing objects
from .forms import EditSceneItem, EditSketchItem, EditEpisodeItem
from .forms import EditProjectItem
from .forms import CommentSketchItem

import cloudinary.uploader
# authentication to lock out wrong users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.db import IntegrityError, DataError


# user enter index.html, expects to see projects
# request.USER for all
@method_decorator(login_required, name='dispatch')
class RenderHomeView(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        # restricts unauthorised accounts from accessing other accounts item(s)
        project_item = ProjectItem.objects.filter(
            project_property_to_director=request.user)

        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
                'create_project_item': CreateProjectItem(),
                'edit_project_item': EditProjectItem(),
                'project_4_header': str(request.user),
            },
        )

    def post(self, request, *args, **kwargs):
        # restricts unauthorised accounts from accessing other accounts item(s)
        project_item = ProjectItem.objects.filter(
            project_property_to_director=request.user)
        project_item_form = CreateProjectItem(data=request.POST)

        # C in "CRUD"
        if project_item_form.is_valid():
            if 'add_project' in request.POST:
                # try and except prevent duplicate auto-generated episode_slug
                try:
                    project = project_item_form.save(commit=False)
            # project_property_to_... create authorisation for project items
                    project.project_property_to_director = request.user
                    project.post = project_item
                    project.project_slug = slugify(str(
                        request.user)+"_"+str(project.project_name))
                    # dev testing
                    print("--- CREATE ---")
                    project.save()
                except IntegrityError:
                    CreateProjectItem()
                except DataError:
                    CreateProjectItem()
                    print("error: project name too long")
        else:
            project_item_form = CreateProjectItem()
            print("failed to create project item")

        # D in "CRUD"
        if 'delete_project' in request.POST:
            delete_project_slug = request.POST.get('delete_project')
            delete_project = ProjectItem.objects.get(
                project_slug=delete_project_slug)
            # dev testing
            print("--- DELETE ---")
            delete_project.delete()

        # U in "CRUD"
        edit_project_item_form = EditProjectItem(data=request.POST)
        if edit_project_item_form.is_valid():
            if 'edit_project' in request.POST:
                edit_project_slug = request.POST.get('edit_project')
                edit_project = ProjectItem.objects.get(
                    project_slug=edit_project_slug)
                # validation exception: less than 79 characters is impossible
                edit_project.project_name = edit_project_item_form.cleaned_data.get(
                    'project_name')
                # dev testing
                print("--- UPDATE ---")
                edit_project.save()

        return render(
            request,
            'index.html',
            {
                'project_item': project_item,
                'create_project_item': CreateProjectItem(),
                'edit_project_item': EditProjectItem(),
            },
        )


# user enter project_view.html, expects to see episodes
@method_decorator(login_required, name='dispatch')
class RenderProjectView(View, LoginRequiredMixin):
    def get(self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(
            ProjectItem, project_slug=project_slug)
        # restricts unauthorised accounts from accessing other accounts item(s)
        episode_item = EpisodeItem.objects.filter(
            episode_property_to_project=project_item,
            episode_property_to_director=request.user)
        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
                'create_episode_item': CreateEpisodeItem(),
                'edit_episode_item': EditEpisodeItem(),
                'episode_4_header': str(project_item),
            },
        )

    def post(self, request, project_slug, *args, **kwargs):
        project_item = get_object_or_404(
            ProjectItem, project_slug=project_slug)
        # restricts unauthorised accounts from accessing other accounts item(s)
        episode_item = EpisodeItem.objects.filter(
            episode_property_to_project=project_item,
            episode_property_to_director=request.user)
        episode_item_form = CreateEpisodeItem(data=request.POST)

        # C in "CRUD"
        if episode_item_form.is_valid():
            if 'add_episode' in request.POST:
                # try and except prevent duplicate auto-generated episode_slug
                try:
                    episode = episode_item_form.save(commit=False)
            # episode_property_to_... create authorisation for episode items
                    episode.episode_property_to_project = project_item
                    episode.episode_property_to_director = request.user
                    episode.episode_slug = slugify(str(
                        project_item.project_slug))+slugify(
                            str(episode.episode_name))
                    episode.post = episode_item
                    # dev testing
                    print("--- CREATE ---")
                    episode.save()
                except IntegrityError:
                    CreateEpisodeItem()
                except DataError:
                    CreateEpisodeItem()
                    print("error: episode name too long")
        else:
            episode_item_form = CreateEpisodeItem()
            print("failed to create episode item")

        # D in "CRUD"
        if 'delete_episode' in request.POST:
            delete_episode_slug = request.POST.get('delete_episode')
            delete_episode = EpisodeItem.objects.get(
                episode_slug=delete_episode_slug)
            # dev testing
            print("--- DELETE ---")
            delete_episode.delete()

        # U in "CRUD"
        edit_episode_item_form = EditEpisodeItem(data=request.POST)
        if edit_episode_item_form.is_valid():
            if 'edit_episode' in request.POST:
                edit_episode_slug = request.POST.get('edit_episode')
                edit_episode = EpisodeItem.objects.get(
                    episode_slug=edit_episode_slug)
                # validation exception: less than 79 characters is impossible
                edit_episode.episode_name = edit_episode_item_form.cleaned_data.get(
                    'episode_name')
                # validation exception: less than 79 characters is impossible
                edit_episode.episode_chronology = edit_episode_item_form.cleaned_data.get(
                    'episode_chronology')
                # dev testing
                print("--- UPDATE ---")
                edit_episode.save()

        return render(
            request,
            'project_view.html',
            {
                'project_item': project_item,
                'episode_item': episode_item,
                'create_episode_item': CreateEpisodeItem(),
                'edit_episode_item': EditEpisodeItem(),
            },
        )


# user enter episode_view.html, expects to see scenes
@method_decorator(login_required, name='dispatch')
class RenderEpisodeView(View, LoginRequiredMixin):
    def get(self, request, episode_slug, *args, **kwargs):
        episode_item = get_object_or_404(
            EpisodeItem, episode_slug=episode_slug)
        # restricts unauthorised accounts from accessing other accounts item(s)
        scene_item = SceneItem.objects.filter(
            scene_property_to_episode=episode_item,
            scene_property_to_director=request.user)
        return render(
            request,
            'episode_view.html',
            {
                'episode_item': episode_item,
                'scene_item': scene_item,
                'create_scene_item': CreateSceneItem(),
                'edit_scene_item': EditSceneItem(),
                'scene_4_header': str(episode_item),
            },
        )

    def post(self, request, episode_slug, *args, **kwargs):
        episode_item = get_object_or_404(
            EpisodeItem, episode_slug=episode_slug)
        # restricts unauthorised accounts from accessing other accounts item(s)
        scene_item = SceneItem.objects.filter(
            scene_property_to_episode=episode_item,
            scene_property_to_director=request.user)
        scene_item_form = CreateSceneItem(data=request.POST)

        # C in "CRUD"
        if scene_item_form.is_valid():
            if 'add_scene' in request.POST:
                # try and except prevent duplicate auto-generated scene_slug
                try:
                    scene = scene_item_form.save(commit=False)
            # scene_property_to_... create authorisation for episode items
                    scene.scene_property_to_episode = episode_item
                    scene.scene_property_to_director = request.user
                    scene.scene_slug = slugify(str(
                        episode_item.episode_slug))+slugify(str(
                            scene.scene_name))
                    scene.post = scene_item
                    # dev testing
                    print("--- CREATE ---")
                    scene.save()
                except IntegrityError:
                    CreateSceneItem()
                except DataError:
                    CreateSceneItem()
                    print("error: scene name too long")
        else:
            scene_item_form = CreateSceneItem()
            print("failed to create scene item")

        # D in "CRUD"
        if 'delete_scene' in request.POST:
            delete_scene_slug = request.POST.get('delete_scene')
            delete_scene = SceneItem.objects.get(scene_slug=delete_scene_slug)
            # dev testing
            print("--- DELETE ---")
            delete_scene.delete()

        # U in "CRUD"
        edit_scene_item_form = EditSceneItem(data=request.POST)
        if edit_scene_item_form.is_valid():
            if 'edit_scene' in request.POST:
                edit_scene_slug = request.POST.get('edit_scene')
                edit_scene = SceneItem.objects.get(scene_slug=edit_scene_slug)
                # validation exception: less than 79 characters is impossible
                edit_scene.scene_name = edit_scene_item_form.cleaned_data.get(
                    'scene_name')
                # validation exception: less than 79 characters is impossible
                edit_scene.scene_chronology = edit_scene_item_form.cleaned_data.get(
                    'scene_chronology')
                # validation exception: less than 79 characters is impossible
                edit_scene.scene_event_notes = edit_scene_item_form.cleaned_data.get(
                    'scene_event_notes')
                # dev testing
                print("--- UPDATE ---")
                edit_scene.save()

        return render(
            request,
            'episode_view.html',
            {
                'episode_item': episode_item,
                'scene_item': scene_item,
                'create_scene_item': CreateSceneItem(),
                'edit_scene_item': EditSceneItem(),
            },
        )


# user enter scene_view.html, expects to see sketches
@method_decorator(login_required, name='dispatch')
class RenderSceneView(View, LoginRequiredMixin):
    def get(self, request, scene_slug, *args, **kwargs):
        scene_item = get_object_or_404(SceneItem, scene_slug=scene_slug)
        # restricts unauthorised accounts from accessing other accounts item(s)
        sketch_item = SketchItem.objects.filter(
            sketch_property_to_scene=scene_item,
            sketch_property_to_director=request.user)

        return render(
            request,
            'scene_view.html',
            {
                'scene_item': scene_item,
                'sketch_item': sketch_item,
                'create_sketch_item': CreateSketchItem(),
                'edit_sketch_item': EditSketchItem(),
                'comment_sketch_item': CommentSketchItem(),
                'sketch_4_header': str(scene_item),
            },
        )

    def post(self, request, scene_slug, *args, **kwargs):
        scene_item = get_object_or_404(SceneItem, scene_slug=scene_slug)
        sketch_item = SketchItem.objects.filter(
            sketch_property_to_scene=scene_item)
        sketch_item_form = CreateSketchItem(request.POST, request.FILES)

        # C in "CRUD"
        if sketch_item_form.is_valid():
            if 'add_sketch' in request.POST:
                # try and except prevent duplicate auto-generated sketch_slug
                try:
                    sketch = sketch_item_form.save(commit=False)
                # scene_property_to_... create authorisation for episode items
                    sketch.sketch_property_to_scene = scene_item
                    sketch.sketch_property_to_director = request.user
                    sketch.post = sketch_item
                    sketch.sketch_slug = slugify(str(
                        request.user))+slugify(str(
                            sketch.sketch_name))
                    # dev testing
                    print("--- CREATE ---")
                    sketch.save()
                except IntegrityError:
                    CreateSketchItem()
                    print("error: duplicate sketch")
                except DataError:
                    CreateSketchItem()
                    print("error: name sketch too long")

        else:
            sketch_item_form = CreateSketchItem()
            print("failed to create sketch item")

        # D in "CRUD"
        if 'delete_sketch' in request.POST:
            delete_sketch_slug = request.POST.get('delete_sketch')
        # restricts unauthorised accounts from accessing other accounts item(s)
            delete_sketch = SketchItem.objects.get(
                sketch_slug=delete_sketch_slug,
                sketch_property_to_director=request.user)
            # dev testing
            print("--- DELETE ---")
            delete_sketch.delete()

        # U in "CRUD"
        edit_sketch_item_form = EditSketchItem(data=request.POST)
        if edit_sketch_item_form.is_valid():
            if 'edit_sketch' in request.POST:
                edit_sketch_slug = request.POST.get('edit_sketch')
                edit_sketch = SketchItem.objects.get(
                    sketch_slug=edit_sketch_slug)
                # validation exception: less than 79 characters is impossible
                edit_sketch.sketch_name = edit_sketch_item_form.cleaned_data.get(
                    'sketch_name')
                # dev testing
                print("--- UPDATE ---")
                edit_sketch.save()

        # U in "CRUD"
        comment_sketch_item_form = CommentSketchItem(data=request.POST)
        if comment_sketch_item_form.is_valid():
            if 'comment_sketch' in request.POST:
                comment_sketch_slug = request.POST.get('comment_sketch')
                comment_sketch = SketchItem.objects.get(
                    sketch_slug=comment_sketch_slug)
                # validation exception: less than 79 characters is impossible
                comment_sketch.sketch_directors_comment = comment_sketch_item_form.cleaned_data.get(
                    'sketch_directors_comment')
                comment_sketch.save()

        return render(
            request,
            'scene_view.html',
            {
                'scene_item': scene_item,
                'sketch_item': sketch_item,
                'create_sketch_item': CreateSketchItem(),
                'edit_sketch_item': EditSketchItem(),
                'comment_sketch_item': CommentSketchItem(),
                'sketch_4_header': str(scene_item),
            },
        )
