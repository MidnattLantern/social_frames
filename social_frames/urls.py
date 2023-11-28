"""
social_frames URL Configuration
"""
from django.contrib import admin
from django.urls import path
from storyboard.views import render_home, render_sign_in, render_sign_out, render_sign_up


"""
If you're new to Django, the first argument with empty string '' is the
Django equivalent to index.html

    social_frames_superuser
    arcanewasamazing420
"""
urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('', render_home, name='home'),
    path('sign_in', render_sign_in, name='sign in'),
    path('sign_out', render_sign_out, name='sign out'),
    path('sign_up', render_sign_up, name='sign up'),
]
