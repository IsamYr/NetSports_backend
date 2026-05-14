from django.contrib import admin
from Social.models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    list_display = ("usuario", "contenido", "fecha")
    search_fields = ("usuario__username", "contenido__titulo")

admin.site.register(Comment, CommentAdmin)