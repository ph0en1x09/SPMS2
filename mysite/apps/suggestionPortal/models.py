from django.db import models
from mysite.models import *
from django.core.validators import *

# Create your models here.

class Feedback(models.Model):
    name = models.CharField('name', max_length = 50, blank = False)
    text = models.CharField('text', max_length = 500, blank = False)
    reply = models.CharField('reply', max_length = 500, default = 'Thanks for your feedback')
    is_read = models.BooleanField(default = False)

    # relationships
    # from mysite.models
    member = models.ManyToManyField(Member)


class Complaint(Feedback):
    # relationships
    # from mysite.models
    coordinator = models.ManyToManyField(Coordinator)
