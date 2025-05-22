from django.shortcuts import render
from .models import Snake


def return_all_snakes(request):
    snake = Snake.objects.all()
    print(snake)
    return render(request, 'all.html', {'snake': snake})


def return_one_snake(request, id):
    snake = Snake.objects.get(id=id)
    return render(request, 'one.html', {'snake': snake})


def sort_snakes_poison(request):
    snake = Snake.objects.filter(poison=1)
    return render(request, 'all.html', {'snake': snake})


def sort_snakes_not_poison(request):
    snake = Snake.objects.filter(poison=0)
    return render(request, 'all.html', {'snake': snake})