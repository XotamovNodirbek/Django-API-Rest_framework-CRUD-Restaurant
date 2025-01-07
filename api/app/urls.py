from django.urls import path
from api.app.views import *
urlpatterns = [
    # Dashboard
    path('dashboard', dashboard, name='dashboard-url'),
    # Category URLs
    path('categories/', category_view, name='categories-url'),
    path('categories/create/', category_create, name='category-create-url'),
    path('categories/update/<int:pk>/', category_update, name='category-update-url'),
    path('categories/delete/<int:pk>/', category_delete, name='category-delete-url'),
    # Food URLs
    path('foods/', food, name='foods-url'),
    path('foods/', food_list, name='foods-list-url'),
    path('food/detail/<int:pk>/', food_detail, name='food-detail-url'),
    path('food/create/', food_create, name='food-create-url'),
    path('food/update/<int:pk>/', food_update, name='food-update-url'),
    path('food/delete/<int:pk>/', food_delete, name='food-delete-url'),
    #Reservations
    path('reservation/', reservation_view, name='reservation_view'),  
    path('reservation/create/', create_reservation, name='reservation_create_url'),  
    path('reservation/update/<int:pk>/', update_reservation, name='reservation_update_url'),  
    path('reservation/delete/<int:pk>/', delete_reservation, name='reservation_delete_url'),  
    #Login
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('continue-cart/', continue_cart, name='sucsess-cart'),  # Continue shopping URL

]
