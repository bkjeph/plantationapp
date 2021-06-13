from django.urls import path
from .views import ProfileView, LoginView, RegisterView, PlantCreateView, PlantDetailView, \
 PlantUpdateView, PlantDeleteView, PlantSearchView
from django.contrib.auth import views as auth_views

urlpatterns = [
 path('plant/', ProfileView.as_view(), name='home'),
 # path('plant/', PlantListView.as_view(), name='plant-list'),
 # path('plant/search', PlantSearchView.as_view(), name='plant-search'),
 path('plant/login/', LoginView.as_view(), name='login'),
 path('plant/logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('plant/profile/', ProfileView.as_view(), name='profile'),
 path('plant/register/', RegisterView.as_view(), name='register'),
 path('plant/create/', PlantCreateView.as_view(), name='plant-create'),
 path('plant/search/', PlantSearchView.as_view(), name='plant-search'),
 path('plant/detail/<int:pk>', PlantDetailView.as_view(), name='plant-detail'),
 # path('plant/<int:pk>/update', PlantUpdateView.as_view(), name='plant-update'),
 # path('plant/<int:pk>/delete', PlantDeleteView.as_view(), name='plant-delete'),
]