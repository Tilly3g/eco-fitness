from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Nutrition, Category

# Create your views here.


def all_nutrition(request):
    """ A view to search for nutrition info and show categories """

    foods = Nutrition.objects.all()
    all_categories = Category.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            foods = foods.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, looks like you didn't search for anything!")
                return redirect(reverse('nutrition'))

            queries = Q(Food__icontains=query) | Q(category__friendly_name__icontains=query)
            foods = foods.filter(queries)

    context = {
        'foods': foods,
        'search_term': query,
        'current_categories': categories,
        'categories': all_categories,
    }

    return render(request, 'nutrition/nutrition.html', context)


def food_item(request, food_id):
    """ A view to show nutritional information for food """

    food = get_object_or_404(Nutrition, pk=food_id)

    context = {
        'food': food,
    }

    return render(request, 'nutrition/food.html', context)
