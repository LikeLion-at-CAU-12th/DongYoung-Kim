from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category = models.CharField(choices=CHOICES, max_length=20)
    thumbnail = models.ImageField(null=True, blank=True, verbose_name="썸네일")

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="test")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Comment(BaseModel):
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='이름', max_length=20)

class Tagging(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    tag = models.ForeignKey('Hashtag', on_delete=models.CASCADE)