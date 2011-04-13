from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from cah.accounts.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext
from cah.accounts.models import FavoriteItem
from cah.meal_plans.models import MealPlan
from cah.menus.models import Menu
from cah.recipes.models import Recipe
from cah.utils.json import JSONResponse

@login_required
def index(request):
#
#    recipes = set(Recipe.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))
#    menus = set(Menu.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))
#    meal_plans = set(MealPlan.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)))
#
#    return render(request, 'accounts/index.html', { 'recipes': recipes, 'menus': menus, 'meal_plans': meal_plans })
    recipes = Recipe.objects.filter(favorited__user=request.user)
    menus = Menu.objects.filter(favorited__user=request.user)
    meal_plans = MealPlan.objects.filter(favorited__user=request.user)
    return render(request, 'accounts/index.html', { 'recipes': recipes, 'menus': menus, 'meal_plans': meal_plans })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email_address'],
                                                password=form.cleaned_data['password1'])
            first_name, last_name = form.cleaned_data['full_name'].split(" ")
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return redirect("signup_success")
    else:
        form = UserCreationForm()
        
    return render_to_response(
        'accounts/signup.html',
        { 'form': form },
        context_instance=RequestContext(request)
    )

def signup_success(request):
    return render(request, 'accounts/signup_success.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = AuthenticationForm()

    return render_to_response(
        'accounts/signin.html',
        { 'form': form },
        context_instance=RequestContext(request)
    )

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@require_POST
@csrf_exempt
@login_required
def favorite_item(request, item_type):
    app_label, model = item_type.split('.')
    content_type = ContentType.objects.get(app_label=app_label, model=model)
    object_id = request.POST.get('id', None)

    if not content_type or not object_id:
        return JSONResponse({
            'status': 'error',
            'reason': 'badly formatted request'
        })

    content_object = content_type.get_object_for_this_type(pk=object_id)

    if not content_object:
        return JSONResponse({
            'status': 'error',
            'reason': 'object doesn\'t exist'
        })

    created = False

    try:
        favorite = FavoriteItem.objects.get(content_type=content_type, object_id=object_id, user=request.user)
        favorite.delete()
    except FavoriteItem.DoesNotExist:
        favorite = FavoriteItem.objects.create(
            user = request.user,
            content_object = content_object
        )
        created = True

    return JSONResponse({
        'status': 'ok',
        'action': 'favorited' if created else 'unfavorited',
        'favorited_object_id': favorite.pk,
    })