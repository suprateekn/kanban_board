from django.urls import path

from task_board.views import UserAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
]
