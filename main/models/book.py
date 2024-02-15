from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    num_copies = models.IntegerField()