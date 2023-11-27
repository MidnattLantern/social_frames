"""
social_frames URL Configuration
"""
from django.contrib import admin
from django.urls import path
from storyboard.views import render_home


"""
If you're new to Django, the first argument with empty string '' is the
Django equivalent to index.html
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home, name='hello')
]
