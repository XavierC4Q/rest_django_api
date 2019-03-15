from .models import Movies 
from rest_framework import serializers
from drf_enum_field.serializers import EnumFieldSerializerMixin

class MoviesSerializer(EnumFieldSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Movies 
        fields = '__all__'