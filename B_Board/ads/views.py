from django.shortcuts import render
from django.views.generic import ListView

from ads.models import Ad


class AdsList(ListView):
    model = Ad
    ordering = '-date_create'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10
