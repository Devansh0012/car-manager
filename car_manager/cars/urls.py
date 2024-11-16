from .import views
from django.urls import path

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
    path('add_car/', views.add_car, name='add_car'),
    path('<int:car_id>/edit_car/', views.edit_car, name='edit_car'),
    path('<int:car_id>/delete_car/', views.delete_car, name='delete_car'),
    path('search_cars/', views.search_cars, name='search_cars'),
    path('my_cars/', views.my_cars, name='my_cars'),
    path('register/', views.register, name='register'),
]