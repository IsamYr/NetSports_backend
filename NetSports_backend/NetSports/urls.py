from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

admin.site.site_header = "NetSports"
admin.site.site_title = "Administración"
admin.site.index_title = "Administración 1.0.0"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Users.urls')),
    path('api/', include('Workout.urls')),
    path('api/', include('Social.urls')),
    path('api/', include('Nutrition.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)