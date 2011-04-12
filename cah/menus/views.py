from django.shortcuts import render
from taggit.models import TaggedItem, Tag
from cah.menus.models import Menu
from cah.utils import paginate

def index(request):
    menus = Menu.objects.all()
    tagged_items = TaggedItem.objects.filter(content_type=19)
    tags = []
    for t in tagged_items:
        tags.append(t.tag)
    tags = set(tags)
    
    return render(request, "menus/index.html", { 'menus': paginate(request, menus), 'all_tags': tags })

def by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    menus = Menu.objects.filter(tags__slug=slug)
    return render(request, "menus/by_tag.html", { 'menus': paginate(request, menus), 'tag': tag })

def detail(request, id):
    menu = Menu.objects.get(pk=id)
    return render(request, "menus/detail.html", { 'menu': menu })