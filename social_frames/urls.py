from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cloudyboard-admin/', admin.site.urls, name='directors_view'),
    path('accounts/', include('allauth.urls')),
    path('', include('storyboard.urls'), name='storyboard_urls'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
