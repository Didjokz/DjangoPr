from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    # Другие маршруты вашего модуля...
]