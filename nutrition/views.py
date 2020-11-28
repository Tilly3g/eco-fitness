from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Nutrition, Category
from .forms import NutritionUpdate

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


@login_required
def add_nutrition(request):
    """ Add nutritional information to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Opps, only administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NutritionUpdate(request.POST)
        if form.is_valid():
            food = form.save()
            messages.success(request, f'Successfully added nutritional information for {food.Food}!')
            return redirect(reverse('nutrition'))
        else:
            messages.error(request, 'Error adding nutritional information. Please ensure the form is valid.')
    else:
        form = NutritionUpdate()

    template = 'nutrition/add_nutrition.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_nutrition(request, food_id):
    """ Edit an existing food """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, only administrators can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Nutrition, pk=food_id)
    if request.method == 'POST':
        form = NutritionUpdate(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated nutritional information for {food.Food}!')
            return redirect(reverse('food_item', args=[food.id]))
        else:
            messages.error(request, 'Error updating nutritional information. Please ensure the form is valid.')
    else:
        form = NutritionUpdate(instance=food)
        messages.info(request, f'You are editing {food.Food}')

    template = 'nutrition/edit_nutrition.html'
    context = {
        'form': form,
        'food': food,
    }

    return render(request, template, context)


@login_required
def delete_nutrition(request, food_id):
    """ Delete nutritional info from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, only administrators can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Nutrition, pk=food_id)
    food.delete()
    messages.success(request, f'Nutritional information deleted for {food.Food}!')
    return redirect(reverse('nutrition'))
