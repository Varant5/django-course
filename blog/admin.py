from django.contrib import admin
from .models import Author, Post, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "excerpt",
        "image",
        "date",
        "slug",
        "content",
        "author",
        "get_tags",
    )
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "user_email", "text")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
