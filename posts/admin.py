from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hashtag)
admin.site.register(Tagging)
admin.site.register(Image)