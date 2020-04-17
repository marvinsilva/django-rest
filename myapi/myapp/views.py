from django.http import HttpResponse
from rest_framework import viewsets, generics

from myapi.myapp.models import Music
from myapi.myapp.serializers import MusicSerializer


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
