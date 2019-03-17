from .models import Movies, User
from rest_framework import serializers
from drf_enum_field.serializers import EnumFieldSerializerMixin

class MoviesSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Movies 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username')