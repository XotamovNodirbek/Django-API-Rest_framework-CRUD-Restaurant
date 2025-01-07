from django.urls import path
from . import views
from .views import add_to_cart, cart_view, cart_remove
urlpatterns = [
    # Category URLs
    path('api/categories/', views.category_list_api, name='category-list-api'),  
    path('api/categories/create/', views.category_create, name='category-create'),  
    path('api/categories/<int:pk>/', views.category_detail, name='category-detail'),  
    path('api/categories/<int:pk>/update/', views.category_update, name='category-update'),  
    path('api/categories/<int:pk>/delete/', views.category_delete, name='category-delete'),  

    # Food URLs
    path('api/foods/', views.food_list, name='food-list'),
    path('api/foods/create/', views.food_create, name='food-create'),
    path('api/foods/<int:pk>/', views.food_detail, name='food-detail'),
    path('api/foods/<int:pk>/update/', views.food_update, name='food-update'),
    path('api/foods/<int:pk>/delete/', views.food_delete, name='food-delete'),

    # Reservation URLs
    path('api/reservations/', views.reservation_list, name='reservation-list'),  
    path('api/reservations/create/', views.reservation_create, name='reservation-create'),
    path('api/reservations/<int:pk>/', views.reservation_detail, name='reservation-detail'),  
    path('api/reservations/<int:pk>/update/', views.reservation_update, name='reservation-update'),  
    path('api/reservations/<int:pk>/delete/', views.reservation_delete, name='reservation-delete'),  

    # Cart URLs
    path('cart/add/<int:food_id>/', add_to_cart, name='add_to_cart'),  
    path('cart/', cart_view, name='cart-view'),  
    path('cart/remove/<int:cart_id>/', cart_remove, name='cart-remove'),  

    # Cart API Views
    path('api/cart/', views.CartListView.as_view(), name='cart-api-list'),
    path('api/cart/create/', views.CartCreateView.as_view(), name='cart-api-create'),  
]
