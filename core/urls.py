from django.urls import include, path

from core.views import *


urlpatterns = [
    path('', index, name='core'),
]
