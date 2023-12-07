from . import views
from django.urls import path

urlpatterns = [
    path('', views.RenderHomeView.as_view(), name='home'),
    path('project', views.RenderProjectView.as_view(), name='project'),
    path('project/episode', views.RenderEpisodeView.as_view(), name='episode'),
    path('project/episode/scene', views.RenderSceneView.as_view(), name='scene'),
]