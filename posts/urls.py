from django.urls import path
from posts.views import *

urlpatterns = [
    path('introduction', introduction_json, name='introduction_json'),
    path('page', page_dynamic, name='page_dynamic'),
    path('<int:id>', get_post_detail, name='게시글 조회'),
    path('tagging', get_tag_relationship, name='get_tag_relationship')
]