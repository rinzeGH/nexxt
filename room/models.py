from django.db import models
from django.db.models import Q
from main.models import Profile


class Room(models.Model):
    slug = models.SlugField(max_length=70, unique=True)

    def related_query(self):
        return self.profile.select_related('grade', 'faculty')


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, related_name='messages', on_delete=models.CASCADE,null=True)
    content = models.TextField(default='',null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ('date_created',)
