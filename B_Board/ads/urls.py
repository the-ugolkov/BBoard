from django.urls import path

from ads.views import AdsList, AdDetail, AdCreate, AdUpdate, AdDelete, ResponseCreate

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    path('create', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/update', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete', AdDelete.as_view(), name='ad_delete'),
    path('<int:pk>/res_create', ResponseCreate.as_view(), name='res_create'),
]
