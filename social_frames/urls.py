#social_frames URL Configuration

from django.contrib import admin
from django.urls import path

#everything productivity:
from storyboard.views import render_home, render_project_view
from storyboard.views import render_episode_view, render_scene_view

#everything regarding account:
from storyboard.views import render_sign_in, render_sign_out, render_sign_up


"""
empty string '' is the Django equivalent to index.html

    social_frames_superuser
    arcanewasamazing420

    social_frames_testuser1
    testpass1
"""

urlpatterns = [
    path('django_admin/', admin.site.urls),

    # account:
    path('sign_in', render_sign_in, name='sign in'),
    path('sign_out', render_sign_out, name='sign out'),
    path('sign_up', render_sign_up, name='sign up'),
    path('accounts', include('allauth.urls')),

    # main:
    path('', render_home, name='home'),
    path('project', render_project_view, name='project'),
    path('project/episode', render_episode_view, name='episode'),
    path('project/episode/scene', render_scene_view, name='scene'),
]
