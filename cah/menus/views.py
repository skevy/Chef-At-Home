from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from taggit.models import TaggedItem, Tag
from cah.menus.models import Menu
from cah.recipes.models import Recipe
from cah.utils import paginate
from cah.utils.json import JSONResponse

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

    delete_permission = False
    if request.user.is_authenticated():
        if menu.user == request.user:
            delete_permission = True
    return render(request, "menus/detail.html", { 'menu': menu, 'can_delete': delete_permission })

@login_required
def add(request):
    context = {}
    if request.method == "POST":
        if request.POST.get('menu_name', None) and request.POST.get('menu_description', None):

            data = {
                'name': request.POST['menu_name'],
                'description': request.POST['menu_description'],
                'user': request.user
            }

            menu = Menu.objects.create(**data)
            menu.tags.add(*([t.strip() for t in request.POST['menu_tags'].split(",")]))

            if request.GET.get('add', None):
                try:
                    r = Recipe.objects.get(pk=request.GET['add'])
                    menu.recipes.add(r)
                    return HttpResponseRedirect("/recipes/%d/" % r.pk)
                except:
                    return HttpResponseRedirect("/menus/")

            return HttpResponseRedirect("/menus/")
        else:
            context['error'] = "Not all fields filled."

    return render(request, "menus/create_menu.html", context)

@login_required
def add_recipe(request, id, recipe_id):
    try:
        menu = Menu.objects.get(pk=id)
        recipe = Recipe.objects.get(pk=recipe_id)
        menu.recipes.add(recipe)

        return redirect('menu_detail', id=id)
    except Exception, e:
        return redirect('recipe_detail', id=recipe_id)

@login_required
def remove_recipe(request, id, recipe_id):
    try:
        menu = Menu.objects.get(pk=id)
        recipe = Recipe.objects.get(pk=recipe_id)
        menu.recipes.remove(recipe)
        
        return redirect('menu_detail', id=id)
    except Exception, e:
        return redirect('menu_detail', id=id)