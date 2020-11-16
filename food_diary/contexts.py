from django.shortcuts import get_object_or_404
from nutrition.models import Nutrition


def get_food(request):

    food_items = []
    calories = 0
    food_amount = 0
    goal = 2000
    total_calories = 0
    diary = request.session.get('food_diary', {})

    for food_id, food_data in diary.items():
        if isinstance(food_data, int):
            food = get_object_or_404(Nutrition, pk=food_id)
            calories = food.Calories / food.Grams * food_data
            total_calories += calories
            food_amount += food_data
            food_items.append({
                'food_id': food_id,
                'amount': food_data,
                'food': food,
                'calories': calories,
            })
        else:
            food = get_object_or_404(Nutrition, pk=food_id)
            for amount in food_data[food_id].items():
                calories = food.Calories / food.Grams * amount
                total_calories += calories
                food_amount += amount
                food_items.append({
                    'food_id': food_id,
                    'amount': amount,
                    'food': food,
                    'calories': calories,
                })

    if total_calories < goal:
        calories_left = int(goal - total_calories)
    else:
        calories_left = "You have reached your calorie goal for today."

    context = {
        'food_items': food_items,
        'food_amount': food_amount,
        'calories': calories,
        'goal': goal,
        'calories_left': calories_left,
    }

    return context
