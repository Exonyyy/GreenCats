from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('forum/', include('forum.urls')),
    path('catalog/', include('catalog.urls'))
]
