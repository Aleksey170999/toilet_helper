from django.contrib import admin
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    path('', views.ToiletListView.as_view(), name='toilet-list'),
    path('<int:pk>/', views.ToiletDetailView.as_view(), name='toilet-detail'),

]