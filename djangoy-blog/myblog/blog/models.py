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
    posts = models.CharField(max_length=300)
    date = models.DateField()

    def __unicode__(self):
        return self.date

    class Meta:
        db_table = 'post'
