from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from posts.models import *

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
    post_detail_json = {
        "id" : post.id,
        "title" : post.title,
        "content" : post.content,
        "writer" : post.writer,
        "category" : post.category,
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : post_detail_json
    })