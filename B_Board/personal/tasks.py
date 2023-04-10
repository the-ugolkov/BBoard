from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from ads.models import Response


def send_message_accept(pk):
    res = Response.objects.get(pk=pk)
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