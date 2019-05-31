from django.contrib import admin
from blog.models import Post,Comment,Post_Like,Comment_Like

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Post_Like)
admin.site.register(Comment_Like)