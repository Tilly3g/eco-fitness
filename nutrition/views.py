from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Nutrition, Category

# Create your views here.


def all_nutrition(request):
    """ A view to search for nutrition info and show categories """

    foods = Nutrition.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            foods = Nutrition.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops, looks like you didn't search for anything!")
                return redirect(reverse('nutrition'))

            queries = Q(food__icontains=query) | Q(category__icontains=query)
            foods = Nutrition.filter(queries)

    context = {
        'foods': foods,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'nutrition/nutrition.html', context)


def product_detail(request, food_id):
    """ A view to show nutrition information for food """

    food = get_object_or_404(Nutrition, pk=food_id)

    context = {
        'food': food,
    }

    return render(request, 'nutrition/food.html', context)
