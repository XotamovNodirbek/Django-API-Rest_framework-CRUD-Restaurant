from django.shortcuts import render, redirect, get_object_or_404
from api.models import Category, Food, Reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .form import ReservationForm

def dashboard(request):
    return render(request, 'index.html')


# Category Views
def category_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('categories-url')


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('categories-url')
    return render(request, 'category_update.html', {'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories-url')


# Food Views
def food(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories
    }
    return render(request, 'food.html', context)

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    context = {
        "food": food,
    }
    return render(request, 'food_detail.html', context)

def food_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        info = request.POST.get('info')
        price = request.POST.get('price')
        discount_percent = request.POST.get('discount_percent')
        photo = request.FILES.get('photo')
        is_food_of_day = request.POST.get('is_food_of_day') == 'on'
        
        Food.objects.create(
            name=name,
            category_id=category_id,
            info=info,
            price=price,
            discount_percent=discount_percent,
            photo=photo,
            is_food_of_day=is_food_of_day
        )
        return redirect('foods-url')
    
    categories = Category.objects.all()
    return render(request, 'food_create.html', {'categories': categories})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    
    if request.method == 'POST':
        food.name = request.POST.get('name')
        food.category_id = request.POST.get('category')
        food.info = request.POST.get('info')
        food.price = request.POST.get('price')
        food.discount_percent = request.POST.get('discount_percent')
        
        if 'photo' in request.FILES:
            food.photo = request.FILES['photo']
            
        food.is_food_of_day = request.POST.get('is_food_of_day') == 'on'
        food.save()
        return redirect('foods-url')

    categories = Category.objects.all()
    context = {
        'food': food,
        'categories': categories
    }
    return render(request, 'food_update.html', context)

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('foods-url')



def food_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')  # URL orqali kelgan kategoriya ID'si

    if category_id:
        # Agar kategoriya tanlangan bo‘lsa, filterlash
        foods = Food.objects.filter(category_id=category_id).order_by('-id')
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        # Agar kategoriya tanlanmagan bo‘lsa, barcha ovqatlarni chiqarish
        foods = Food.objects.all().order_by('-id')
        selected_category = None

    context = {
        'foods': foods,
        'categories': categories,
        'selected_category': selected_category
    }
    return render(request, 'foods.html', context)


# Login views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard-url')
            else:
                return HttpResponse('Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')



def reservation_view(request):
    reservations = Reservation.objects.all()  # Fetch all reservations
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the reservation to the database
            return redirect('reservation_view')  # Redirect to the same page to refresh the list
    else:
        form = ReservationForm()

    # Pass the reservations and the form to the template
    return render(request, 'reservation.html', {'form': form, 'reservations': reservations})

# View to create a reservation (used in the modal form)
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_view')  # Redirect to reservations page after saving
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()  # Save the updated reservation
            return redirect('reservation_view')  # Redirect to the reservation list
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation_update.html', {'form': form, 'reservation': reservation})

# Delete Reservation
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()  # Delete the reservation
    return redirect('reservation_view')  # Redirect to the res