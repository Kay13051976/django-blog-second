from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
# This will register both our post model and post admin class with our admin site
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
