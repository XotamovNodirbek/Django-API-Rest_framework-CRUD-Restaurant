from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('api/categories/', views.category_list_api, name='category-list-api'),  # Get all categories (API)
    path('api/categories/create/', views.category_create, name='category-create'),  # Create category
    path('api/categories/<int:pk>/', views.category_detail, name='category-detail'),  # Get category detail
    path('api/categories/<int:pk>/update/', views.category_update, name='category-update'),  # Update category
    path('api/categories/<int:pk>/delete/', views.category_delete, name='category-delete'),  # Delete category

    # Food URLs
    path('api/foods/', views.food_list, name='food-list'),  # Get all foods
    path('api/foods/create/', views.food_create, name='food-create'),  # Create food
    path('api/foods/<int:pk>/', views.food_detail, name='food-detail'),  # Get food detail
    path('api/foods/<int:pk>/update/', views.food_update, name='food-update'),  # Update food
    path('api/foods/<int:pk>/delete/', views.food_delete, name='food-delete'),  # Delete food

    # Reservation URLs
    path('api/reservations/', views.reservation_list, name='reservation-list'),  # Get all reservations
    path('api/reservations/create/', views.reservation_create, name='reservation-create'),  # Create reservation
    path('api/reservations/<int:pk>/', views.reservation_detail, name='reservation-detail'),  # Get reservation detail
    path('api/reservations/<int:pk>/update/', views.reservation_update, name='reservation-update'),  # Update reservation
    path('api/reservations/<int:pk>/delete/', views.reservation_delete, name='reservation-delete'),  # Delete reservation

    # Cart URLs
    path('cart/add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),  # Add food to cart
    path('cart/', views.cart_view, name='cart-view'),  # View cart (renamed from add_to_cart)
    path('cart/remove/<int:cart_id>/', views.cart_remove, name='cart-remove'),  # Remove item from cart

    # Cart API Views
    path('api/cart/', views.CartListView.as_view(), name='cart-api-list'),  # Cart list (API)
    path('api/cart/create/', views.CartCreateView.as_view(), name='cart-api-create'),  # Create cart item (API)
]
