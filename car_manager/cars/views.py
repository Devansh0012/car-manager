from django.shortcuts import render
from .models import Car
from .forms import CarForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm

def index(request):
    return render(request, 'cars/index.html')

def car_list(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/add_car.html', {'form': form})

@login_required
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_deleted.html', {'car': car})

def search_cars(request):
    query = request.GET.get('query', '')
    cars = Car.objects.filter(name__icontains=query) if query else Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


@login_required
def my_cars(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/car_list.html', {'cars': cars})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('car_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
