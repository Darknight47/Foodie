from django.contrib import admin

from comments.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "date_added")

# Register your models here.

admin.site.register(Comment, CommentAdmin)