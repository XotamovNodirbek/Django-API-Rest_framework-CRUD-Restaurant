from .models import *
from rest_framework import serializers, viewsets
from rest_framework import serializers
from .models import Cart, Food

# Serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'category', 'info', 'price', 'discounted_price', 'photo', 'is_food_of_day']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' 



class CartSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.name', read_only=True)  # Oziq-ovqat nomi
    food_price = serializers.DecimalField(source='food.price', read_only=True, max_digits=8, decimal_places=2)  # Oziq-ovqat narxi
    discounted_price = serializers.SerializerMethodField()  # Chegirmali narx

    class Meta:
        model = Cart
        fields = ['id', 'food', 'food_name', 'food_price', 'discounted_price', 'quantity']

    def get_discounted_price(self, obj):
        # Agar oziq-ovqatda chegirma bo'lsa, chegirmali narxni hisoblash
        if obj.food.discount_percent:
            return obj.food.price - (obj.food.discount_percent * obj.food.price / 100)
        return obj.food.price  # Agar chegirma yo'q bo'lsa, asl narxni qaytarish
