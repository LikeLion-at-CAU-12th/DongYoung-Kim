from django.urls import path
from posts.views import *

urlpatterns = [
    # path('introduction', introduction_json, name='introduction_json'),
    # path('page', page_dynamic, name='page_dynamic'),
    path('', PostList.as_view(), name='get_posts_last_week'),
    path('<int:id>/', PostDetail.as_view(), name='get_post_by_id'),
    path('<int:id>/comment', CommentList.as_view(), name='get_comment_all'),
    # path('tagging', get_tag_relationship, name='get_tag_relationship'),
]