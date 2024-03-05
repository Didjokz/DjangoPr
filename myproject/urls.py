from django.contrib import admin
from django.urls import path

from django.urls import include, path

urlpatterns = [
    # Другие маршруты...
    path('posts/', include('post.urls')),
    path('', include('mainpage.urls')),
]