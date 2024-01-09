from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get("pk"))
