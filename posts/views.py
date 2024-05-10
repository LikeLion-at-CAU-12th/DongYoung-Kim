from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *
from django.utils import timezone
from datetime import timedelta

from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

class PostDetail(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = self.get_serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostList(generics.GenericAPIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        last_week = request.query_params.get('last_week', False)

        if last_week == 'True' or last_week == 'true':
            one_week_ago = timezone.now() - timedelta(days=7)
            posts_last_week = Post.objects.filter(
                created_at__gte=one_week_ago
            ).order_by("-created_at")

            serializer = self.get_serializer(posts_last_week, many=True)
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = self.get_serializer(posts, many=True)
            return Response(serializer.data)

class CommentList(APIView):
    def get(self, request, id):
        comments = Comment.objects.filter(post=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)