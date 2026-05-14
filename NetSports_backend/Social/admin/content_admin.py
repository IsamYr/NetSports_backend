from django.contrib import admin
from Social.models import Content

class ContentAdmin(admin.ModelAdmin):
    def total_likes(self, obj):
        return obj.likes.count()

    def total_comments(self, obj):
        return obj.comments.count()

    def total_favourites(self, obj):
        return obj.favourites.count()

    total_likes.short_description = "Likes"

    list_display = ("usuario", "descripcion", "fecha_publicacion", "total_likes", "total_comments", "total_favourites", "fecha_actualizacion")
    search_fields = ("descripcion", "usuario__username")
    list_filter = ("fecha_publicacion",)
    inlines = []


admin.site.register(Content, ContentAdmin)