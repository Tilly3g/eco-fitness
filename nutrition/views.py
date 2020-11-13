from django.shortcuts import render
from .models import Nutrition

# Create your views here.


def all_nutrition(request):

    foods = Nutrition.objects.all()

    context = {
        'foods': foods,
    }

    return render(request, 'nutrition/nutrition.html', context)
