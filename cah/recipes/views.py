from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from taggit.models import Tag, TaggedItem
from cah.recipes.models import Recipe, Ingredient

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
    context = {}
    if request.method == "POST":
        if request.POST.get('recipe_name', None) and request.POST.get('recipe_description', None) and request.POST.get('directions', None):

            data = {
                'name': '',
                'description': '',
                'user': request.user,
                'directions': request.POST.directions
            }

            recipe = Recipe.objects.create(**data)
            recipe.tags.add(*([t.strip() for t in request.POST['recipe_tags'].split(",")]))

            #ingredients
            num_ingredients = request.POST['num_ingredients']
            ingredients = []
            for t in range(0, num_ingredients):
                i = Ingredient.objects.create(
                    recipe=recipe,
                    quantity=request.POST['ingredient_%d_quantity' % t],
                    description=request.POST['ingredient_%d_description' % t]
                )

            return HttpResponseRedirect("/recipes/")
        else:
            context['error'] = "Not all fields filled."

    context['initial_ingredients'] = [0, 1, 2, ]

    return render(request, "recipes/add_recipe.html", context)