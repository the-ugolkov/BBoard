from django.contrib import admin

from ads.models import Ad, AdContent, Response

admin.site.register(Ad)
admin.site.register(AdContent)
admin.site.register(Response)
