from django.db import models

from django.contrib.auth.models import User
from cah.menus.models import Menu

class Recipe(models.Model):
    menu = models.ForeignKey(Menu, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    
    directions = models.TextField()
    
class RecipeMedia(models.Model):
    recipe = models.ForeignKey(Recipe)
    caption = models.CharField(max_length=200)
    
    class Meta:
        abstract = True
        
class RecipePhoto(RecipeMedia):
    orig_photo = models.ImageField(upload_to="recipes/photos/orig/")
    thumbnail = models.ImageField(upload_to="recipes/photos/thumb/")

class RecipeVideo(RecipeMedia):
    pass
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients")
    quantity = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200)