from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from nutrition.models import Nutrition

# Create your views here.

def view_diary(request):
    """ A view that renders the diary contents page """

    return render(request, 'food_diary/diary.html')


def add_to_diary(request, food_id):
    """ Add amount of the specified food to the diary """

    food = get_object_or_404(Nutrition, pk=food_id)
    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    diary = request.session.get('food_diary', {})

    if food_id in list(diary.keys()):
        diary[food_id] += amount
        messages.success(request, f'Updated {food.Food} amount to {diary[food_id]}g')
    else:
        diary[food_id] = amount
        messages.success(request, f'Added {food.Food} to your diary')

    request.session['food_diary'] = diary
    return redirect(redirect_url or '/')


def remove_from_diary(request, food_id):
    """Remove the food item from the diary completely"""

    try:
        food = get_object_or_404(Nutrition, pk=food_id)
        diary = request.session.get('food_diary', {})

        diary.pop(food_id)
        messages.success(request, f'Removed {food.Food} from your food diary')

        request.session['food_diary'] = diary
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing food item: {e}')
        return HttpResponse(status=500)
