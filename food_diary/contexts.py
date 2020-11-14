
def snacks(request):

    food_items = []
    calories = 0
    goal = 0

    if calories < goal:
        calories_left = goal - calories
    else:
        calories_left = "You have reached your calorie gaol for snacks today."

    context = {
        'food_items': food_items,
        'calories': calories,
        'goal': goal,
        'calories_left': calories_left,
    }

    return context


def breakfast(request):

    food_items = []
    calories = 0
    goal = 0

    if calories < goal:
        calories_left = goal - calories
    else:
        calories_left = "You have reached your calorie gaol for breakfast today."

    context = {
        'food_items': food_items,
        'calories': calories,
        'goal': goal,
        'calories_left': calories_left,
    }

    return context


def lunch(request):

    food_items = []
    calories = 0
    goal = 0

    if calories < goal:
        calories_left = goal - calories
    else:
        calories_left = "You have reached your calorie gaol for lunch today."

    context = {
        'food_items': food_items,
        'calories': calories,
        'goal': goal,
        'calories_left': calories_left,
    }

    return context


def dinner(request):

    food_items = []
    calories = 0
    goal = 0

    if calories < goal:
        calories_left = goal - calories
    else:
        calories_left = "You have reached your calorie gaol for dinner today."

    context = {
        'food_items': food_items,
        'calories': calories,
        'goal': goal,
        'calories_left': calories_left,
    }

    return context
