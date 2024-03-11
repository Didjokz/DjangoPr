from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    # Другие маршруты вашего модуля...
]