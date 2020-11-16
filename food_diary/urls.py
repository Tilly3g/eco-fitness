from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_diary, name='diary'),
    path('add/<food_id>/', views.add_to_diary, name='add_to_diary'),
]
