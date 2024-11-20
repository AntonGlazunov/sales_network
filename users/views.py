
from rest_framework_simplejwt.views import TokenObtainPairView
from users.permissions import IsAuthenticatedAndActive
from users.serializers import MyTokenObtainPairSerializer


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
