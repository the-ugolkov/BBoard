from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from ads.forms import AdsForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object().id
        responses = Response.objects.filter(ad=ad)
        context['response'] = responses
        return context


class AdCreate(LoginRequiredMixin, CreateView):
    form_class = AdsForm
    model = Ad
    template_name = 'ads/ads_create.html'


class AdUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdsForm
    model = Ad
    template_name = 'ads/ads_create.html'


class AdDelete(DeleteView):
    model = Ad
    template_name = 'ads/ad_delete.html'
    success_url = reverse_lazy('ads_list')


# def accepted(request):
#     ad = Ad.objects.get(id=request.)
