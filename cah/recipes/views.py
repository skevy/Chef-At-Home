from django.shortcuts import render

def index(request):
    return render(request, "recipes/index.html", {})
    
def detail(request):
    return render(request, "recipes/detail.html", {})
    
def add(request):
    
    first_name = "Adam"
    last_name = "Miskiewicz"
    
    user = {
        'first_name': first_name,
        'last_name': last_name,
    }
    
    context = {
    'initial_ingredients':['ingredient1','ingredient2','ingredient3'],
    'user': user
    
    }
    return render(request, "recipes/add_recipe.html", context)