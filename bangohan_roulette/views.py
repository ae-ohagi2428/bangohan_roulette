import random
from django.shortcuts import render, get_object_or_404
from .models import Dish

def roulette(request):
    return render(request, 'bangohan_roulette/roulette.html')

def result(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    ingredients = dish.ingredients.all()
    return render(request, 'bangohan_roulette/result.html', {
        'dish': dish,
        'ingredients': ingredients,
    })

def random_dish(request):
    from django.http import JsonResponse
    dishes = Dish.objects.all()
    if not dishes:
        return JsonResponse({'error': '料理が登録されていません'}, status=404)
    dish = random.choice(list(dishes))
    return JsonResponse({'dish_id': dish.id, 'dish_name': dish.name})