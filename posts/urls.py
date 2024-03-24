from django.urls import path
from posts.views import *

urlpatterns = [
    path('introduction', introduction_json, name='introduction_json'),
    path('page', page_dynamic, name='page_dynamic'),
]