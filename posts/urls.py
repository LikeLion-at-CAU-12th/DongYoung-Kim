from django.urls import path
from posts.views import *

urlpatterns = [
    path('introduction', introduction_json, name='introduction_json'),
]