from django.urls import path

from ads.views import AdsList, AdDetail

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    # path('<int:pk>', ResponseList.as_view(), name='response_list')
]
