from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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