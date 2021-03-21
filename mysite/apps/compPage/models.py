from django.db import models
from django.core.validators import *

# Create your models here.

class Competition(models.Model):
    name = models.CharField('name', max_length = 100, blank = False)


class Game(models.Model):
    age = models.IntegerField('age', blank = False)
    gender = models.CharField('gender', max_length=10, blank = False)
    game_type = models.CharField('type', max_length=100, blank = False)

    # relationships
    competition = models.ForeignKey(Competition, on_delete = models.CASCADE, null = True)

from mysite.models import NewUser

class Ticket(models.Model):
    num_tickets = models.IntegerField('num_tickets', validators=[MaxValueValidator(4)], default=1)

    # relationships
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE, null = True)
    competition = models.ForeignKey(Competition, on_delete = models.CASCADE, null = True)
