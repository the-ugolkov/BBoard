from django.urls import path

from personal.views import IndexView, ResponseList, ResponseDelete, accept

urlpatterns = [
    path('accounts/', IndexView.as_view(), name='account'),
    path('accounts/responses/', ResponseList.as_view(), name='responses'),
    path('accounts/responses/<int:pk>/delete', ResponseDelete.as_view(), name='response_delete'),
    path('accounts/responses/<int:pk>/accept', accept, name='res_accept'),
]
