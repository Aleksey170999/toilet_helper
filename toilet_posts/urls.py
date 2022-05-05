from django.urls import path
from . import views


urlpatterns = [
    path('', views.ToiletListView.as_view(), name='toilet-list'),
    path('<int:pk>/', views.ToiletDetailView.as_view(), name='toilet-detail'),
    path('map/', views.default_map, name='toilet-map'),

]

