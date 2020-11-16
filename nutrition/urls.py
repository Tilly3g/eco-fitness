from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_nutrition, name='nutrition'),
    path('<food_id>', views.food_item, name='food_item')
]
