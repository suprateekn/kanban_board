from django.urls import path

from task_board.views import UserAPIView, UserLoginAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
