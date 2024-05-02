from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *
from django.utils import timezone
from datetime import timedelta

from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def introduction_json(request):
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '메시지 전달 성공!',
            'data': [
                {
                    "name": "김동영",
                    "grade": 3,
                    "major": "Software"
                },
                {
                    "name": "정현수",
                    "grade": 2,
                    "major": "Library and Information Science"
                }
            ]
        })
    
def page_dynamic(request):
    if request.method == "GET":
        context = {
            'me' : {
                'name' : '김동영',
                'age' : 24,
                'major' : 'Software',
                'github' : 'Temple2001'
            },
            'reviewer' : {
                'name' : '정현수',
                'age' : 22,
                'major' : 'Library and Information Science',
                'github' : 'usernamehs'
            }
        }
        return render(request, 'page.html', context)

@require_http_methods(["GET"])
def get_post_detail(request,id):
    post = get_object_or_404(Post, pk=id)
    image_models = Image.objects.filter(post=id)
    image_list = {image_model.id:image_model.img.url for image_model in image_models}

    post_detail_json = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "writer": post.writer.username,
        "category": post.category,
        "images": image_list,
    }

    return render(request, 'post.html', post_detail_json)

@require_http_methods(["GET"])
def get_tag_relationship(request):
    res = {
        'status': 200,
        'mesasge': '게시글-해시태그 관계 조회 성공',
        'data': {},
    }
    taggings = Tagging.objects.all()
    for tagging in taggings:
        res['data'][tagging.id] = {
            'post_id': tagging.post_id,
            'post 이름': Post.objects.get(id=tagging.post_id).title,
            'tag_id': tagging.tag_id,
            'tag 이름': Hashtag.objects.get(id=tagging.tag_id).name,
        }
    return JsonResponse(res)

# @require_http_methods(["GET"])
# def get_comments(request, id):
#     if request.method == "GET":
#         comments_in_post = Comment.objects.filter(post=id)
#         comment_json_list = []
#
#         for comment in comments_in_post:
#             comment_json = {
#                 'id': comment.id,
#                 'content': comment.content,
#                 'writer': comment.writer.username,
#                 'post': comment.post.title,
#             }
#             comment_json_list.append(comment_json)
#
#         return JsonResponse({
#             'status': 200,
#             'message': '댓글 목록 조회 성공',
#             'data': comment_json_list,
#         })

class CommentList(APIView):
    def get(self, request, id):
        comments = Comment.objects.filter(post=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@require_http_methods(["GET"])
def get_posts_last_week(request):
    if request.method == "GET":
        one_week_ago = timezone.now() - timedelta(days=7)
        posts_last_week = Post.objects.filter(
            created_at__gte=one_week_ago
        ).order_by("-created_at")

        post_json_list = []

        for post in posts_last_week:
            post_json = {
                "id" : post.id,
                "title" : post.title,
                "content" : post.content,
                "writer" : post.writer.username,
                "category" : post.category,
                "created_at": post.created_at,
            }
            post_json_list.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': '최근 일주일 동안 작성된 게시글 목록 조회 성공',
            'data': post_json_list,
        })