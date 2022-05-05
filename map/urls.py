from django.urls import path
from . import views


urlpatterns = [
    path('', views.map_view_all_markers, name="map-view"),
    path('<int:pk>/', views.map_view_detail, name="map-view-detail"),

]

