from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'author'


class Post(models.Model):
    user = models.ForeignKey('Author')
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'post'
