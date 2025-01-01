from django.urls import path
from api.app.views import *

urlpatterns = [
    # Dashboard
    path('admin', dashboard, name='dashboard-url'),  # Bosh sahifa

    # Category URLs
    path('categories/', category_view, name='categories-url'),  # Kategoriyalar ro'yxati
    path('categories/create/', category_create, name='category-create-url'),  # Yangi kategoriya qo'shish
    path('categories/update/<int:pk>/', category_update, name='category-update-url'),  # Kategoriyani yangilash
    path('categories/delete/<int:pk>/', category_delete, name='category-delete-url'),  # Kategoriyani o'chirish

    # Food URLs
    path('foods/', food, name='foods-url'),  # Ovqatlar ro'yxati
    path('food/detail/<int:pk>/', food_detail, name='food-detail-url'),
    path('food/create/', food_create, name='food-create-url'),  # Yangi ovqat qo'shish
    path('food/update/<int:pk>/', food_update, name='food-update-url'),  # Ovqatni yangilash
    path('food/delete/<int:pk>/', food_delete, name='food-delete-url'),  # Ovqatni o'chirish
    #Login
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    #Cart

]
