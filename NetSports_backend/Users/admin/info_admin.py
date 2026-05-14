from django.contrib import admin

from Users.models import InfoPersonal

class InfoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellidos', 'telefono', 'fecha_nacimiento', 'altura_cm', 'peso_kg')
    list_filter = ('fecha_nacimiento', 'apellidos')
    readonly_fields = ('fecha_union',)
    search_fields = ('telefono', 'apellidos')

    fieldsets = (
        ("Información personal", {'fields': ('nombre', 'apellidos', 'telefono', 'fecha_nacimiento')}),
        ("Reconocimiento físico", {'fields': ('altura_cm', 'peso_kg')}),
        ("Extra", {'fields': ('fecha_union',)}),
        ("Usuario", {'fields': ('usuario',)}),
    )

admin.site.register(InfoPersonal, InfoAdmin)