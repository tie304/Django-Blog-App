# Create your models here.
import django
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateTimeField('date published', default=django.utils.timezone.now)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=200)
    likes = models.ManyToManyField(Post)

