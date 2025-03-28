from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer


class UserCreation(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
