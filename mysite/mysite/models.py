from django.db import models
from django.contrib.auth.models import User, Group, Permission, UserManager, AbstractUser
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
    competition = models.OneToOneField(Competition, on_delete = models.SET_NULL, null = True, blank=True)
    game = models.ManyToManyField(Game, blank=True)

    # from coursePage models.py
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True, blank=True)

    # from partyPage.models
    event = models.OneToOneField(Event, on_delete = models.SET_NULL, null = True, blank=True)

class NewUser(User):
    objects = UserManager()
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
    courses = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True, blank=True)

    # from partyPage.models
    event = models.OneToOneField(Event, on_delete = models.SET_NULL, null = True, blank=True)

    # relationships for coordinator
    # from coursePage.models
    courses = models.ForeignKey(Course, on_delete = models.SET_NULL, null = True, blank=True)


class MemberManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, *kwargs).filter(type=NewUser.Types.MEMBER)


class CoordinatorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, *kwargs).filter(type=NewUser.Types.COORDINATOR)


class CommitteeManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, *kwargs).filter(type=NewUser.Types.COMMITTEE)


class ManagerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, *kwargs).filter(type=NewUser.Types.MANAGER)


class Member(NewUser):
    objects = MemberManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = NewUser.Types.MEMBER
        return super().save(*args, **kwargs)


class Coordinator(NewUser):
    is_coordinator = True
    objects = CoordinatorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = NewUser.Types.COORDINATOR
        return super().save(*args, **kwargs)


class Committee(NewUser):
    is_committee = True
    objects = CommitteeManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = NewUser.Types.COMMITTEE
        return super().save(*args, **kwargs)


class Manager(NewUser):
    is_superuser = True
    objects = ManagerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = NewUser.Types.MANAGER
        return super().save(*args, **kwargs)
