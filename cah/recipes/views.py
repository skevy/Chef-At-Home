from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from taggit.models import Tag, TaggedItem
from cah.recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    tagged_items = TaggedItem.objects.filter(content_type=11)
    tags = []
    for t in tagged_items:
        tags.append(t.tag)
    tags = set(tags)
    return render(request, "recipes/index.html", { 'recipes': recipes, 'all_tags': tags })

def by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    recipes = Recipe.objects.filter(tags__slug=slug)
    return render(request, "recipes/by_tag.html", { 'recipes': recipes, 'tag': tag })
    
def detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    return render(request, "recipes/detail.html", { 'recipe': recipe })

@login_required
def add(request):
    context = {
        'initial_ingredients':['ingredient1','ingredient2','ingredient3'],
    }
    return render(request, "recipes/add_recipe.html", context)