from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Author, Toilet


class ToiletListView(ListView):
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_list.html'


class ToiletDetailView(DetailView):
    model = Toilet
    fields = '__all__'
    template_name = 'toiletmodel_detail.html'