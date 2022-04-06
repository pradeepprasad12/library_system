from bookaccount.models import Post
from bookaccount.api.serializers import UserSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated ,DjangoModelPermissions

class Userviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)