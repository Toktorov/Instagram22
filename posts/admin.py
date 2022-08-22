from django.contrib import admin
from posts.models import Post, PostComment, PostLike

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)