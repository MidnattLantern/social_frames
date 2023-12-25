from . import views
from django.urls import path


# name_view/ enables Social Frames to differenciate from i.e project_slug and episode_slug
urlpatterns = [
    path('', views.RenderHomeView.as_view(), name='home_url_path'),
    path('project_view/<slug:project_slug>/', views.RenderProjectView.as_view(), name='project_url_path'),
    path('episode_view/<slug:episode_slug>/', views.RenderEpisodeView.as_view(), name='episode_url_path'),
    path('scene_view/<slug:scene_slug>/', views.RenderSceneView.as_view(), name='scene_url_path'),
]