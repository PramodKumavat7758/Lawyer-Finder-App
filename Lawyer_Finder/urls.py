from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from Lawyer_Finder import settings

urlpatterns = [
    path('dash/', admin.site.urls),
    path('user/', include('user.urls')),
    path('lawyer/',include('lawyer.urls')),

    path('dash/',include('admin_dashboard.urls')),
path('', include('user.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)