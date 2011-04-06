from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()