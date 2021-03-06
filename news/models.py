from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=1200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
