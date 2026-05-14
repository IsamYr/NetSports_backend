from django.contrib import admin
from Social.models import Like

class LikeInline(admin.TabularInline):
    model = Like
    extra = 0

class LikeAdmin(admin.ModelAdmin):
    list_display = ("usuario", "contenido")

admin.site.register(Like, LikeAdmin)