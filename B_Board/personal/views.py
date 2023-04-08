from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView
from django_filters.views import FilterView

from B_Board import settings
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

    html_content = render_to_string(
        'response_accepted.html',
        {
            'response': res,
            'link': f'{settings.SITE_URL}/ads/{res.ad.pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Здравствуй {res.author}',
        body=res.text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[res.author.email],
    )
    msg.attach_alternative(html_content, "text/html")

    msg.send()

    message = 'Вы приняли отзыв '
    return render(request, 'personal/accept.html', {'response': res, 'message': message})
