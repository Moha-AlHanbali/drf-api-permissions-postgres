from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, BooleanField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey


class Insect(models.Model):
    name = CharField(max_length = 64)
    can_fly = BooleanField()
    number_of_legs = IntegerField()
    description = TextField()
    author = ForeignKey(User, on_delete = CASCADE)

    def __str__(self):
        return self.name