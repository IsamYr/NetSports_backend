from django.contrib import admin

from Users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'visibilidad', 'profile_photo')
    list_filter = ('visibilidad',)
    search_fields = ('usuario__email', 'usuario__username')
    ordering = ('usuario__email', 'usuario__username')

    fieldsets = (
        ("Información", {'fields': ('biografia', 'visibilidad', 'profile_photo')}),
        ("Usuario", {'fields': ('usuario',)}),
    )

admin.site.register(Profile, ProfileAdmin)