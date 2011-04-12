from django.shortcuts import render
from taggit.models import TaggedItem, Tag
from cah.meal_plans.models import MealPlan
from cah.utils import paginate

def index(request):
    meal_plans = MealPlan.objects.all()
    tagged_items = TaggedItem.objects.filter(content_type=22)
    tags = []
    for t in tagged_items:
        tags.append(t.tag)
    tags = set(tags)
    return render(request, "meal_plans/index.html", { 'meal_plans': paginate(request, meal_plans), 'all_tags': tags })

def by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    meal_plans = MealPlan.objects.filter(tags__slug=slug)
    return render(request, "meal_plans/by_tag.html", { 'meal_plans': paginate(request, meal_plans), 'tag': tag })

def detail(request, id):
    meal_plan = MealPlan.objects.get(pk=id)
    return render(request, "meal_plans/detail.html", { 'meal_plan': meal_plan })