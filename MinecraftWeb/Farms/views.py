from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Farm
from .forms import RegisterForm, ContactForm

def home(request):
    farms = Farm.objects.all()

    # Apply filtering based on the GET parameters
    farm_type = request.GET.get('farm_type')
    rating = request.GET.get('rating')
    difficulty = request.GET.get('difficulty')
    order_by_rates = request.GET.get('order_by_rates')

    if farm_type:
        farms = farms.filter(farm_type=farm_type)

    if rating:
        farms = farms.filter(overall_rating=rating)

    if difficulty:
        farms = farms.filter(difficulty=difficulty)

    # Sort by rates if specified
    if order_by_rates == "desc":
        farms = sorted(farms, key=lambda x: int(x.rates) if x.rates.isdigit() else 0, reverse=True)
    elif order_by_rates == "asc":
        farms = sorted(farms, key=lambda x: int(x.rates) if x.rates.isdigit() else 0)

    return render(request, 'home.html', {'farms': farms})


def about(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'farm_detail.html', {'farm': farm})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or home after submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

