from django.contrib import admin
from . models import Food, Category, Reservation, User, Cart
# Register your models here.
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Reservation)