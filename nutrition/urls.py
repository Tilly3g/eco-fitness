from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_nutrition, name='nutrition'),
    path('<food_id>', views.food_item, name='food_item'),
    path('add/', views.add_nutrition, name='add_nutrition'),
    path('edit/<int:food_id>/', views.edit_nutrition, name='edit_nutrition'),
    path('delete/<int:food_id>/', views.delete_nutrition, name='delete_nutrition'),
]
