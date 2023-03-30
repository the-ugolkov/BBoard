from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ads.models import Ad, Response


class AdsList(ListView):
    model = Ad
    ordering = '-date_create'
    template_name = 'ads/ads.html'
    context_object_name = 'ads'
    paginate_by = 10


class AdDetail(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'


# class ResponseList(ListView):
#     model = Response
#     ordering = '-date_create'
#     template_name = 'ads/ad.html'
#     context_object_name = 'response'
#     paginate_by = 10