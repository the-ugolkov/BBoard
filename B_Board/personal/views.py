from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from ads.models import Response, Ad


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/index.html'


class ResponseList(ListView):
    model = Response
    template_name = 'personal/response_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = Response.objects.filter(ad__author__username=self.request.user.username)
        print(queryset)
        return queryset


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset.filter(ad__author__username=self.request.user.username))
    #     return queryset.filter(ad__author__username=self.request.user.username)

