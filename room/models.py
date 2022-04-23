from django.db import models
from django.db.models import Q
from main.models import Profile



class Room(models.Model):
    slug = models.SlugField(max_length=70, unique=True)

    def related_query(self):
        return self.profile.select_related('grade', 'faculty')


class Message(models.Model):
    pass
