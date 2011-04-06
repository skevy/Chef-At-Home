from django.db import models
from cah.menus.models import Menu

class MealPlan(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    menus = models.ManyToManyField(Menu, blank=True, null=True)