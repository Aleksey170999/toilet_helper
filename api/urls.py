from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('toilets/list/', views.ToiletListView.as_view()),
    path('toilets/create/', views.ToiletCreateView.as_view()),
    path('toilets/list/<int:tg_id>/', views.ToiletListView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
