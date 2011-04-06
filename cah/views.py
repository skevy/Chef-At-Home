from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import auth
from django.shortcuts import render
from cah.meal_plans.models import MealPlan
from cah.menus.models import Menu
from cah.recipes.models import Recipe

def index(request):
    if request.user.is_authenticated():
        template_name = "index_signedin.html"
    else:
        template_name = "index_signedout.html"
    return render(request, template_name, {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def search(request):
    q = request.GET.get('q', None)
    if q:
        recipes = set(Recipe.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))
        menus = set(Menu.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))
        meal_plans = set(MealPlan.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))

        return render(request, 'search.html', { 'recipes': recipes, 'menus': menus, 'meal_plans': meal_plans })
    else:
        return HttpResponseNotFound()