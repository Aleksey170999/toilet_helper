from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from toilets import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('toilet-list'), permanent=False)),
    path('admin/', admin.site.urls),
    path('toilets/', include('toilet_posts.urls')),
    path('api/', include('api.urls')),
    path('map/', include("map.urls")),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
