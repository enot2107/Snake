from django.contrib import admin
from .models import Snake, Category


@admin.register(Snake)
class SnakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'description', 'image', 'cost', 'birthdate', 'poison', 'gender']


@admin.register(Category)
class CategorySnakeAdmin(admin.ModelAdmin):
    list_display = ['name']

