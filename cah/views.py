from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import auth
from django.shortcuts import render
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
    query = request.GET.get('q', None)
    if query:
        recipes = Recipe.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        menus = Menu.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        meal_plans = MealPlan.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))

        return render(request, 'search.html', { 'recipes': recipes, 'menus': menus, 'meal_plans': meal_plans })
    else:
        return HttpResponseNotFound()