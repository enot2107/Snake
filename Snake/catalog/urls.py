from django.urls import path
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.return_all_snakes, name='return_all_snakes'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('one/<int:id>/', views.return_one_snake, name='return_one_snake'),
    path('poison/', views.sort_snakes_poison, name='sort_snakes_poison'),
    path('notpoison/', views.sort_snakes_not_poison, name='sort_snakes_not_poison'),
   ]