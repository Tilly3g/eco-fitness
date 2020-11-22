from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bookings, name='bookings'),
    path('<int:session_id>/', views.session_info, name='session_info'),
    path('add/', views.add_session, name='add_session'),
    path('edit/<int:session_id>/', views.edit_session, name='edit_session'),
    path('delete/<int:session_id>/', views.delete_session, name='delete_session'),
]
