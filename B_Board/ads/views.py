from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from ads.forms import AdsForm, ResForm
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
        path = self.request.user
        print(path)
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


class ResponseCreate(LoginRequiredMixin, CreateView):
    form_class = ResForm
    nodel = Response
    template_name = 'ads/res_create.html'
    success_url = reverse_lazy('ads_list')

    def form_valid(self, form):
        response = form.save(commit=False)
        if self.request.method == 'POST':
            pk = self.request.path.split('/')[-2]
            username = self.request.user
            response.ad = Ad.objects.get(id=pk)
            response.author = User.objects.get(username=username)
        response.save()
        return super().form_valid(form)


    # message = 'Вы подписаны на категорию '
    # return render(request, 'subscribe.html', {'category': category, 'message': message})
