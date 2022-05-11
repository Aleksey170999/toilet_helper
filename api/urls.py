from django.conf.urls.static import static
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('toilets/list/', views.ToiletListView.as_view()),
    path('toilets/create/', views.ToiletCreateView.as_view()),
    path('toilets/list/<int:tg_id>/', views.ToiletListViewPersonolized.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'deocument_root': settings.MEDIA_ROOT})
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)