from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('toilet-list'), permanent=False)),
    path('admin/', admin.site.urls),
    path('toilets/', include('toilet_posts.urls')),
    path('api/', include('api.urls')),
    path('map/', include("map.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),

    ]
