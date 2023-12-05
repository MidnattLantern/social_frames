#social_frames URL Configuration

from django.contrib import admin
from django.urls import path, include

#everything productivity:
from storyboard.views import render_home, render_project_view
from storyboard.views import render_episode_view, render_scene_view

#outdated:
# from storyboard.views import render_sign_in, render_sign_out, render_sign_up


"""
empty string '' is the Django equivalent to index.html

    social_frames_superuser
    arcanewasamazing420

    social_frames_testuser1
    testpass1

    testuser2
    testpass2
"""

urlpatterns = [
    path('backrooms_staff_only/', admin.site.urls),

    # account:
    path('accounts/', include('allauth.urls')),

    # main:
    path('', render_home, name='home'),
    path('project', render_project_view, name='project'),
    path('project/episode', render_episode_view, name='episode'),
    path('project/episode/scene', render_scene_view, name='scene'),
]
