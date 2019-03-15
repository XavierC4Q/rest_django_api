from django.db import models

from enumfields import EnumField
from enumfields import Enum

class Genres(Enum):
    HORROR = 'Horror'
    ACTION_ADVENTURE = 'Action / Adventure'
    DRAMA = 'Drama'
    ROMANCE = 'Romance'
    DOCUMENTARY = 'Documentary'

class Movies(models.Model):

    genre = EnumField(Genres)
    title = models.TextField(default='', null=True, blank=True, max_length=100)
    release_data = models.DateField()


    

