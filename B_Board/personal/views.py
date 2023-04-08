from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView
from django_filters.views import FilterView

from ads.models import Response
from personal.filters import ResponseFilter
from personal.forms import ResponseForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'personal/index.html'


class ResponseList(LoginRequiredMixin, FilterView):
    form_class = ResponseForm
    model = Response
    template_name = 'personal/response_list.html'
    context_object_name = 'responses'
    filterset_class = ResponseFilter

    # def get_queryset(self):
    #     print(self.request.user)
    #     queryset = Response.objects.filter(ad__author__username=self.request.user)
    #     self.filterset = ResponseFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super().get_filterset_kwargs(filterset_class)
        kwargs['user'] = self.request.user
        return kwargs


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'personal/response_delete.html'
    success_url = reverse_lazy('responses')


@login_required
def accept(request, pk):
    res = Response.objects.get(id=pk)
    res.accepted()

    message = 'Вы приняли отзыв '
    return render(request, 'personal/accept.html', {'response': res, 'message': message})
