from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Другие маршруты...
    path('admin/', admin.site.urls),
    path('me/', include('mypage.urls')),
    path('posts/', include('post.urls')),
    path('', include('mainpage.urls')),
]