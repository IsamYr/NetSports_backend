from django.contrib import admin
from Social.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('destinatario', 'emisor', 'tipo', 'leida', 'fecha_creacion')
    search_fields = ('destinatario', 'emisor', 'fecha_creacion')
    list_filter = ('tipo', 'fecha_creacion')

admin.site.register(Notification, NotificationAdmin)