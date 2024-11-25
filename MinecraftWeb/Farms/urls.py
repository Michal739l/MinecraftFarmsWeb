from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('farm/<int:pk>/', views.farm_detail, name='farm_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('remove-farm/', views.remove_farm, name='remove_farm'),
    path('add_farm/', views.add_farm, name='add_farm'),
    path('nether_calculator/', views.nether_calculator, name='nether_calculator'),
]