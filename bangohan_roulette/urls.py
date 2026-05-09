from django.urls import path
from . import views

app_name = 'bangohan_roulette'

urlpatterns = [
    path('', views.roulette, name='roulette'),
    path('result/<int:dish_id>/', views.result, name='result'),
    path('random/', views.random_dish, name='random_dish'),
]