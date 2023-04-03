from django.urls import path

from personal.views import IndexView, ResponseList

urlpatterns = [
    path('accounts/', IndexView.as_view(), name='account'),
    path('accounts/responses/', ResponseList.as_view(), name='responses')
]
