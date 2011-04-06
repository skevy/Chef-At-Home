from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db import models
from cah.menus.models import Menu

class MealPlan(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    tags = TaggableManager()
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    menus = models.ManyToManyField(Menu, blank=True, null=True)

    def get_image(self):
        image = None
        try:
            image = self.menus.all()[0].recipes.all()[0].get_image()
        except:
            pass
        return image