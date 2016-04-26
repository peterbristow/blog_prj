from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):

# author is linked to a registered user in the "auth_user" table
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
