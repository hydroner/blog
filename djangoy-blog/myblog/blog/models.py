from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.CharField(max_length=10)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'post'
