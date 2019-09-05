from django.http import JsonResponse
from rest_framework import generics

from task_board.login_signup_serializer import UserSerializer, User


class UserAPIView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return JsonResponse(user.data, safe=False)
        return JsonResponse("Invalid Request", safe=False)
