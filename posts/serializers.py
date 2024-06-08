from rest_framework import serializers
from .models import Comment, Post
from rest_framework.exceptions import ValidationError
from PIL import Image
import io

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_thumbnail(self, value):
        if value and value.content_type == 'image/png':
            raise ValidationError("PNG 형식의 이미지는 업로드할 수 없습니다.")
        elif value:
            img = Image.open(value)
            width, height = img.size
            img_small = img.resize((width//2, height//2))
            img_io = io.BytesIO()
            img_small.save(img_io, format=img.format)
            value.file = img_io
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"