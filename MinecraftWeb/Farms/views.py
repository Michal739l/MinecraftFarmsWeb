from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Farm
from .forms import FarmForm
from django.db.models import Q


def home(request):
    query = request.GET.get('q')
    if query:
        farms = Farm.objects.filter(Q(name__icontains=query) | Q(location__icontains=query))
    else:
        farms = Farm.objects.all()
    return render(request, 'home.html', {'farms': farms})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def add_farm(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.owner = request.user
            farm.save()
            return redirect('home')
    else:
        form = FarmForm()
    return render(request, 'farm_form.html', {'form': form})

def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'farm_detail.html', {'farm': farm})

@user_passes_test(lambda u: u.is_superuser)
def add_farm(request):
    # Logic to handle adding a farm
    pass