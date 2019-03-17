from django.shortcuts import render
from .models import Movies, User
from .serializers import MoviesSerializer, UserSerializer
from rest_framework import mixins, generics

class MovieListView(generics.ListCreateAPIView):
    
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class UserListView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer