#social_frames URL Configuration

from django.contrib import admin
from django.urls import path, include
# from 18 dec guide
from django.conf import settings
from django.conf.urls.static import static

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
    path('directors_view/', admin.site.urls, name='directors_view'),
    path('accounts/', include('allauth.urls')),
    path('', include('storyboard.urls'), name='storyboard_urls'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
