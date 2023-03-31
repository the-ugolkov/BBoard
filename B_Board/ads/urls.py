from django.urls import path

from ads.views import AdsList, AdDetail, AdCreate

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    path('<create>', AdCreate.as_view(), name='ad_create'),
]
