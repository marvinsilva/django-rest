from rest_framework import serializers
from myapi.myapp.models import Music, Band, Album, Member


class MusicSerializer(serializers.ModelSerializer):
    album = serializers.ReadOnlyField(source='album.title')

    class Meta:
        model = Music
        fields = ('id', 'title', 'seconds', 'album')


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    band = serializers.ReadOnlyField(source='band.name')

    class Meta:
        model = Album
        fields = ('id', 'title', 'band', 'date')


class MemberSerializer(serializers.ModelSerializer):
    band = serializers.ReadOnlyField(source='band.name')

    class Meta:
        model = Member
        fields = ('id', 'name', 'age', 'band')
