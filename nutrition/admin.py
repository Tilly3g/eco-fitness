from django.contrib import admin
from .models import Nutrition, Category

# Register your models here.


class NutritionAdmin(admin.ModelAdmin):
    list_display = (
        "Food",
        "Grams",
        "Calories",
        "Protein",
        "Fat",
        "Saturated_Fat",
        "Fiber",
        "Carbs",
        "category",
    )

    ordering = ('Food',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Category, CategoryAdmin)
