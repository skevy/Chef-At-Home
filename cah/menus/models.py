from django.db import models

from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cah.recipes.models import Recipe

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = TaggableManager()
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    recipes = models.ManyToManyField(Recipe, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_image(self):
        image = None
        try:
            image = self.recipes.all()[0].get_image()
        except:
            pass
        return image