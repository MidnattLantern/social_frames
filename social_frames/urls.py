#social_frames URL Configuration

from django.contrib import admin
from django.urls import path, include

#everything productivity:
#from storyboard.views import render_home_view, render_project_view
#from storyboard.views import render_episode_view, render_scene_view

#outdated:
# from storyboard.views import render_sign_in, render_sign_out, render_sign_up


"""
empty string '' is the Django equivalent to index.html

    social_frames_superuser
    arcanewasamazing420

    testuser2
    testpass2
"""

urlpatterns = [
    path('staff_only/', admin.site.urls),

    # account:
    path('accounts/', include('allauth.urls')),

    # non pythonic (attempting to remove)
#    path('', render_home_view, name='home'),
#    path('project', render_project_view, name='project'),
#    path('project/episode', render_episode_view, name='episode'),
#    path('project/episode/scene', render_scene_view, name='scene'),

    # pythonic object oriented (attempting to make functional)
    path('', include('storyboard.urls'), name='storyboard-urls'),
]
