from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Plant


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class SearchPlantForm(forms.Form):
    search_string = forms.CharField(label='plantation search', max_length=100)


# class AddPlantForm(forms.ModelForm):
#     class Meta:
#         model = Plant
#         fields = ('name', 'usage', 'pruning', 'pest_management', 'fertiliser', 'water_requirement',
#                   'sunlight', 'humidity', 'temperature', 'effect_on_wild_life', 'effect_on_microclimate',
#                   'effect_on_soil', 'average_height', 'canopy_density', 'canopy_radius', 'root_structure',
#                   'harvesting_method', 'post_harvest_care', 'nutrition_requirements', 'soil_type',
#                   'sprouting_conditions', 'planting_method', 'distance_between_plats', 'pruning',
#                   'pest_management', 'fertiliser', 'water_requirement')
#


