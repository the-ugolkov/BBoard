from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView

from ads.models import Response
from personal.forms import ResponseForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/index.html'


class ResponseList(ListView):
    form_class = ResponseForm
    model = Response
    template_name = 'personal/response_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = Response.objects.filter(ad__author__username=self.request.user.username)
        return queryset


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'personal/response_delete.html'
    success_url = reverse_lazy('responses')