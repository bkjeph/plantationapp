from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import Plant
from datetime import timedelta
from django.utils import timezone
from datetime import date
from datetime import datetime
from .filters import PlantFilter
from .forms import SearchPlantForm
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin




# @method_decorator(login_required, name='dispatch')
# # @login_required(login_url='/login/')
# class PlantListView(ListView):
#
#     model = Plant
#     template_name = 'plantation/list.html'
#     context_object_name = 'plants'
#     paginate_by = 5
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(PlantListView, self).get_context_data(**kwargs)
#         plants = self.get_queryset()
#         page = self.request.GET.get('page')
#         paginator = Paginator(plants, self.paginate_by)
#         try:
#             plants = paginator.page(page)
#         except PageNotAnInteger:
#             plants = paginator.page(1)
#         except EmptyPage:
#             plants = paginator.page(paginator.num_pages)
#         context['plants'] = plants
#         print(plants)
#         return context
#
#
#     def get_queryset(self):
#         return Plant.objects.all()
#
#     def dispatch(self, request, *args, **kwargs):
#         return super(LoginPage, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
# @login_required(login_url='/login/')
class PlantCreateView(CreateView):
    model = Plant
    template_name = 'plantation/create.html'
    fields = ['name', 'usage', 'pruning', 'pest_management', 'fertiliser', 'water_requirement', 'sunlight',
              'humidity', 'temperature', 'effect_on_wild_life', 'effect_on_microclimate', 'effect_on_soil',
              'average_height', 'canopy_density', 'canopy_radius', 'root_structure', 'harvesting_method',
              'post_harvest_care', 'nutrition_requirements', 'soil_type', 'sprouting_conditions', 'planting_method',
              'distance_between_plats']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.email = self.request.user
        return super(PlantCreateView, self).form_valid(form)




@method_decorator(login_required, name='dispatch')
# @login_required(login_url='/login/')
class PlantDetailView(DetailView):

    model = Plant
    template_name = 'plantation/detail.html'
    context_object_name = 'plant'


class PlantSearchView(LoginRequiredMixin, View):
    template_name = 'plantation/search.html'
    model = Plant
    context_object_name = 'plants'
    paginate_by = 3

    def get(self, request):
        print("inside search view")
        query_string = request.GET.get('q')
        if query_string:
            plants = Plant.objects.filter(name__icontains=query_string)
        else:
            plants = None
        context = {
          'plants': plants,

        }
        return render(request, 'plantation/search.html', context)


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PlantSearchView, self).get_context_data(**kwargs)
    #     query_string = self.request.GET.get('q')
    #     page = self.request.GET.get('page')
    #     if query_string:
    #         plants = self.model.objects.filter(name__icontains=query_string)
    #     else:
    #         plants = self.model.objects.all()
    #     # paginator = Paginator(plants, self.paginate_by)
    #     # try:
    #     #     plants = paginator.page(page)
    #     # except PageNotAnInteger:
    #     #     plants = paginator.page(1)
    #     # except EmptyPage:
    #     #     plants = paginator.page(paginator.num_pages)
    #     context['plants'] = plants
    #     return context



    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     if query:
    #         object_list = self.model.objects.filter(name__icontains=query)
    #     else:
    #         object_list = self.model.objects.all()
    #     return object_list




@method_decorator(login_required, name='dispatch')
class PlantUpdateView(UpdateView):

    model = Plant
    template_name = 'plantation/update.html'
    context_object_name = 'plantation'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('plant-detail', kwargs={'pk': self.object.id})



@method_decorator(login_required, name='dispatch')
class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plantation/delete.html'
    success_url = reverse_lazy('plant-search')



class RegisterView(View):
    def get(self, request):
        return render(request, 'plantation/register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'plantation/register.html', { 'form': form })


class LoginView(View):
    def get(self, request):
        return render(request, 'plantation/login.html', { 'form':  AuthenticationForm() })

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'plantation/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'plantation/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return render(request, 'plantation/login.html', {'form': AuthenticationForm(), 'messages': ['Authentication Failed!!!']})


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        print("inside profile view")
        print(request.user)
        plants = Plant.objects.filter(email=request.user)
        context = {
          'plants': plants,

        }
        return render(request, 'plantation/profile.html', context)










#
#
# # signup page
# def RegisterPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, "Account was created for " + user)
#                 return redirect('login')
#
#         context = {'form': form}
#         return render(request, 'register.html', context)
#
#
# # login page
# def LoginPage(request):
#     if request.user.is_authenticated:
#         return redirect('plant-search')
#     else:
#
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('plant-search')
#             else:
#                 messages.info(request, 'Username or password is incorrect')
#         context = {}
#         return render(request, 'login.html', context)
#
#
# # logout page
# def LogOutPage(request):
#     logout(request)
#     return redirect('login')

#
# # for selecting food each day
# @login_required
# def select_food(request):
#     person = Profile.objects.filter(person_of=request.user).last()
#     # for showing all food items available
#     food_items = Food.objects.filter(person_of=request.user)
#     form = SelectFoodForm(request.user, instance=person)
#
#     if request.method == 'POST':
#         form = SelectFoodForm(request.user, request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = SelectFoodForm(request.user)
#
#     context = {'form': form, 'food_items': food_items}
#     return render(request, 'select_food.html', context)
#
#
# def add_plant(request):
#     form = AddPlantForm(request.POST)
#     if request.method == 'POST':
#         form = AddPlantForm(request.POST)
#         if form.is_valid():
#             plantation = form.save(commit=False)
#             plantation.user_info = User.objects.create_user(email=request.email)
#             plantation.save()
#             return redirect('add_plant')
#     else:
#         form = AddPlantForm()
#
#     # for filtering plantation
#     context = {'form': form}
#     return render(request, 'add_plant.html', context)
#
#
# # for updating food given by the user
# @login_required
# def update_food(request, pk):
#     food_items = Food.objects.filter(person_of=request.user)
#
#     food_item = Food.objects.get(id=pk)
#     form = AddFoodForm(instance=food_item)
#     if request.method == 'POST':
#         form = AddFoodForm(request.POST, instance=food_item)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     myFilter = FoodFilter(request.GET, queryset=food_items)
#     context = {'form': form, 'food_items': food_items, 'myFilter': myFilter}
#
#     return render(request, 'add_plant.html', context)
#
#
# # for deleting food given by the user
# @login_required
# def delete_food(request, pk):
#     food_item = Food.objects.get(id=pk)
#     if request.method == "POST":
#         food_item.delete()
#         return redirect('profile')
#     context = {'food': food_item, }
#     return render(request, 'delete_food.html', context)
#
#
# # profile page of user
# @login_required
# def ProfilePage(request):
#     # getting the lastest profile object for the user
#     person = Profile.objects.filter(person_of=request.user).last()
#     food_items = Food.objects.filter(person_of=request.user)
#     form = ProfileForm(instance=person)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=person)
#
#     # querying all records for the last seven days
#     some_day_last_week = timezone.now().date() - timedelta(days=7)
#     records = Profile.objects.filter(date__gte=some_day_last_week, date__lt=timezone.now().date(),
#                                      person_of=request.user)
#
#     context = {'form': form, 'food_items': food_items, 'records': records}
#     return render(request, 'profile.html', context)