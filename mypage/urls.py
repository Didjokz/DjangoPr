from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    # Другие маршруты вашего модуля...
]