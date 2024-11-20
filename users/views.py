
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserCreateSerializer, MyTokenObtainPairSerializer


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()