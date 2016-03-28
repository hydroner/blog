from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'post'
