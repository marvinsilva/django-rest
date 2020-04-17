from django.http import HttpResponse
from rest_framework import viewsets

from myapi.myapp.models import Music
from myapi.myapp.serializers import MusicSerializer


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')


class MusicListViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
