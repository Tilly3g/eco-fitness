from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_diary, name='diary'),
    path('add/<food_id>/', views.add_to_diary, name='add_to_diary'),
    path('remove/<food_id>/', views.remove_from_diary, name='remove_from_diary'),
]
