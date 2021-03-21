from django.db import models
from mysite.models import *
from django.core.validators import *

# Create your models here.
class Course(models.Model):
    name = models.CharField('name', max_length=20, blank=False)
    num_students = models.IntegerField('num_students', validators=[MaxValueValidator(50)], default=0)

    
