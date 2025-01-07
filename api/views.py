from django.shortcuts import render, get_object_or_404, redirect
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Food, Reservation, Cart
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
@api_view(["GET"])  
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['PUT'])
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return Response({'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def food_list(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def food_create(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    serializer = FoodSerializer(food)
    return Response(serializer.data)

@api_view(['PUT'])
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    serializer = FoodSerializer(food, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return Response({'message': 'Food deleted'}, status=status.HTTP_204_NO_CONTENT)

# Reservation Views
@api_view(['GET'])
def reservation_list(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def reservation_create(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

@api_view(['PUT'])  
def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    serializer = ReservationSerializer(reservation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])  
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return Response({'message': 'Reservation deleted'}, status=status.HTTP_204_NO_CONTENT)


@login_required
def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart_item, created = Cart.objects.get_or_create(food=food, user=request.user, defaults={'quantity': 1})

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart-view')  

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'card.html', {'cart_items': cart_items})

@login_required
def cart_remove(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart-view')


class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





