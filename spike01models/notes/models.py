from django.db import models

# Create your models here.

MAX_TEXT_LENGTH = 250 + 5

class Note(models.Model):
    text = models.CharField(max_length=MAX_TEXT_LENGTH, default='')
    created = models.DateTimeField('created', auto_now=True)
    updated = models.DateTimeField('updated', auto_now=True)


class Comment(models.Model):
    text = models.CharField(max_length=MAX_TEXT_LENGTH, default='')
    created = models.DateTimeField('created', auto_now=True)
    updated = models.DateTimeField('updated', auto_now=True)
    parent = models.ForeignKey(Note, on_delete=models.CASCADE, default=None)
