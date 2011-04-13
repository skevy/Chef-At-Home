from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cah.accounts.models import FavoriteItem

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = TaggableManager()
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    favorited = generic.GenericRelation(FavoriteItem)
    
    directions = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.name)

    def get_image(self):
        image = None
        recipe_media = self.photos.all()
        try:
            image = recipe_media[0]
        except:
            pass
        return image

class RecipePhoto(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="photos")
    caption = models.CharField(max_length=200)
    orig_photo = models.ImageField(upload_to="recipes/photos/orig/")
    thumbnail = models.ImageField(upload_to="recipes/photos/thumb/")

class RecipeVideo(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="videos")
    caption = models.CharField(max_length=200)
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients")
    quantity = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200)