from django.shortcuts import render
from .models import Movies
from .serializers import MoviesSerializer
from rest_framework import mixins, generics

class MovieListView(generics.ListCreateAPIView):
    
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
