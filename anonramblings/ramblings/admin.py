
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    ordering = ("-created_at", )
    list_display = ("title", "permlink", "nickname", "created_at", "sent_to_blockchain", "is_deleted", "comment_count")
    list_filter = ("is_deleted", "sent_to_blockchain")
    search_fields = ("title", "body")

admin.site.register(Post, PostAdmin)