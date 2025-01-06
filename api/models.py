from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    info = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    photo = models.ImageField(upload_to='media/food/')
    is_food_of_day = models.BooleanField(default=False)

    def discounted_price(self):
        if self.discount_percent:
            discounted_price = self.price - self.discount_percent * self.price / 100
            return discounted_price
        return self.price

    def __str__(self):
        return self.name



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    number_of_guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.food.name

class User(AbstractUser):
    USER_ROLE = [
        ("admin", "Admin"),
        ("user", "User"),
    ]
    
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_role = models.CharField(max_length=100, choices=USER_ROLE, default='user')

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.first_name
