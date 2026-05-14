from django.contrib import admin
from Social.models import Favourite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("usuario", "contenido")

admin.site.register(Favourite, FavoriteAdmin)