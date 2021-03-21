from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _
from apps.compPage.models import *
from apps.coursePage.models import *
from apps.partyPage.models import *

#Create your models here
class Slot(models.Model):
    from_time = models.TimeField('from_time', max_length=10, blank=False)
    to_time = models.TimeField('to_time', max_length=10, blank=False)
    date = models.DateField('date', max_length=20, blank=False)
    num_participants = models.IntegerField('num_participants', default=0)

    # relationships
    # from compPage models.py
    competition = models.OneToOneField(Competition, on_delete = models.SET_NULL, null = True)
    game = models.ManyToManyField(Game)

    # from coursePage models.py
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True)

    # from partyPage.models
    event = models.OneToOneField(Event, on_delete = models.SET_NULL, null = True)

class NewUser(User):
    class Types(models.TextChoices):
        MEMBER = "MEMBER", "Member"
        COORDINATOR = "COORDINATOR", "Coordinator"
        COMMITTEE = "COMMITTEE", "Committee"
        MANAGER = "MANAGER", "Manager"

    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.MEMBER)
    name = models.CharField('name', max_length=50, blank=False)
    age = models.IntegerField('age', blank=False)
    gender = models.CharField('gender', max_length=10, blank=False)
    is_superuser = False
    is_coordinator = False
    is_committee = False
    is_active = True

    # relationships for Member
    # from coursePage.models
    courses = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True)

    # from partyPage.models
    event = models.OneToOneField(Event, on_delete = models.SET_NULL, null = True)

    # relationships for coordinator
    # from coursePage.models
    courses = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True)


class Member(NewUser):
    class Meta:
        proxy = True


class Coordinator(NewUser):
    is_coordinator = True

    class Meta:
        proxy = True


class Committee(NewUser):
    is_committee = True

    class Meta:
        proxy = True


class Manager(NewUser):
    is_superuser = True

    class Meta:
        proxy = True
