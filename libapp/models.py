from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=80)
    pic = models.CharField(max_length=80)
