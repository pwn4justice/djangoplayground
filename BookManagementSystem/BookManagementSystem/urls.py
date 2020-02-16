from django.contrib import admin
from django.urls import path, include
from . import settings

# static files handle part:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
]

#urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
