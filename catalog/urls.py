from django.urls import path
from .views import *


urlpatterns = [
    path('', catalog, name='catalog'),
    path('<name>', structure_info, name='structure-info')
]
