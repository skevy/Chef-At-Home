from django.contrib import admin

from cah.recipes.models import *

class RecipePhotoInline(admin.TabularInline):
    model = RecipePhoto

class RecipeVideoInline(admin.TabularInline):
    model = RecipeVideo

class IngredientInline(admin.TabularInline):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, RecipePhotoInline, RecipeVideoInline, ]

admin.site.register(Recipe, RecipeAdmin)

