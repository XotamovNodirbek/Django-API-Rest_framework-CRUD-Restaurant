from django import forms
from api.models import Reservation
from api.models import Food, Category

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'number_of_guests', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'category', 'info', 'price', 'discount_percent', 'photo', 'is_food_of_day']


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )