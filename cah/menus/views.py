from django.shortcuts import render
from taggit.models import TaggedItem
from cah.menus.models import Menu

def index(request):
    recipes = Menu.objects.all()
    tagged_items = TaggedItem.objects.filter(content_type=19)
    tags = []
    for t in tagged_items:
        tags.append(t.tag)
    tags = set(tags)
    return render(request, "menus/index.html", { 'menus': recipes, 'all_tags': tags })

def by_tag(request, slug):
    recipes = Menu.objects.filter(tags__slug=slug)
    return render(request, "menus/by_tag.html", { 'menus': recipes })

def detail(request, id):
    recipe = Menu.objects.get(pk=id)
    return render(request, "menus/detail.html", { 'menus': recipe })