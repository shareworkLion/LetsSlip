from django.contrib import admin
from .models import Post, Comment, CommentReply, Profile

admin.site.register(Post)
admin.site.register(CommentReply)
admin.site.register(Comment)
admin.site.register(Profile)