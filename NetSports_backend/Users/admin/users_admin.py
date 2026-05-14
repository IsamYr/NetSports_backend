from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import InfoPersonal, Usuario, Profile

class InfoPersonalInline(admin.StackedInline):
    model = InfoPersonal
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 0
    verbose_name = "Información personal"

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    min_num = 1
    max_num = 1
    extra = 0
    verbose_name = "Perfil personal"

class UsuarioAdmin(UserAdmin):
    inlines = [InfoPersonalInline, ProfileInline]

    list_display = ('email', 'username', 'is_active') # Columnas
    list_filter = ('is_active', 'is_superuser') # Barra de filtro
    search_fields = ('email', 'username') # Barra de búsqueda
    ordering = ('-email',)

    fieldsets = ( # Para modificar la tabla
        ("Inicio de sesión", {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )
    add_fieldsets = ( # Al crear una nueva tabla
        ("Información de inicio de sesión", {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        ("Configuración", {
            'classes': ('wide',),
            'fields': ('is_active', 'is_superuser', 'is_staff',)}
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)