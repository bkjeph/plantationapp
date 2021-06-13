from django.db import models
import enum
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.

PLANTING_METHOD_CHOICES = (
    ("Direct Seeds", "Direct Seeds"),
    ("Grafting", "Grafting"),
    ("Cuttings", "Cuttings")
)


CANOPY_DENSITY_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class PlantingMethod(enum.Enum):
    DIRECT_SEEDS = "Direct seeds"
    GRAFTING = "Grafting"
    CUTTINGS = "Cuttings"


class CanopyDensity(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class User(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=256)


class CareRequired(models.Model):
    pruning = models.CharField(max_length=256, null=True)
    pest_management = models.CharField(max_length=256, null=True)
    fertiliser = models.CharField(max_length=256, null=True)
    water_requirement = models.CharField(max_length=256, null=False)


class HowToPlant(models.Model):
    sprouting_conditions = models.CharField(max_length=256, null=True)
    planting_method = models.CharField(max_length=40, choices=PLANTING_METHOD_CHOICES, null=False)
    distance_between_plats = models.FloatField(verbose_name="in cms")


class SoilRequirements(models.Model):
    nutrition_requirements = models.CharField(max_length=256, null=False)
    soil_type = models.CharField(max_length=512, null=True)


class HarvestingCare(models.Model):
    harvesting_method = models.CharField(max_length=1024, null=False)
    post_harvest_care = models.CharField(max_length=1024, null=False)


class PlanDimensions(models.Model):
    average_height = models.FloatField(verbose_name="in cms")
    canopy_density = models.IntegerField(choices=CANOPY_DENSITY_CHOICES)
    canopy_radius = models.FloatField()
    root_structure = models.CharField(max_length=1024)


class EnvironmentalEffects(models.Model):
    effect_on_wild_life = models.CharField(max_length=1024)
    effect_on_microclimate = models.CharField(max_length=1024)
    effect_on_soil = models.CharField(max_length=1024)


class ClimateRequirements(models.Model):
    sunlight = models.CharField(max_length=256)
    humidity = models.CharField(max_length=256)
    temperature = models.FloatField(verbose_name="in Celsius")


class Plant(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=256, null=False)
    usage = models.CharField(max_length=1024, null=True)
    pruning = models.CharField(max_length=256, null=True)
    pest_management = models.CharField(max_length=256, null=True)
    fertiliser = models.CharField(max_length=256, null=True)
    water_requirement = models.CharField(max_length=256, null=True)
    sunlight = models.CharField(max_length=256, null=True)
    humidity = models.CharField(max_length=256, null=True)
    temperature = models.FloatField(verbose_name="in Celsius", null=True)
    effect_on_wild_life = models.CharField(max_length=1024, null=True)
    effect_on_microclimate = models.CharField(max_length=1024, null=True)
    effect_on_soil = models.CharField(max_length=1024, null=True)
    average_height = models.FloatField(verbose_name="in cms", null=True)
    canopy_density = models.IntegerField(choices=CANOPY_DENSITY_CHOICES, null=True)
    canopy_radius = models.FloatField(null=True)
    root_structure = models.CharField(max_length=1024, null=True)
    harvesting_method = models.CharField(max_length=1024, null=True)
    post_harvest_care = models.CharField(max_length=1024, null=True)
    nutrition_requirements = models.CharField(max_length=256, null=True)
    soil_type = models.CharField(max_length=512, null=True)
    sprouting_conditions = models.CharField(max_length=256, null=True)
    planting_method = models.CharField(max_length=40, choices=PLANTING_METHOD_CHOICES, null=True)
    distance_between_plats = models.FloatField(verbose_name="in cms", null=True)
    timestamp = models.DateField(auto_now_add=True, null=True)
    email = models.CharField(max_length=256, null=True)

# class Plant(models.Model):
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     name = models.CharField(max_length=256, null=False)
#     usage = models.CharField(max_length=1024, null=False)
#     care_required = models.OneToOneField(
#         CareRequired,
#         on_delete=models.CASCADE
#     )
#     climate_requirements = models.OneToOneField(
#         ClimateRequirements,
#         on_delete=models.CASCADE
#     )
#     environmental_effects = models.OneToOneField(
#         EnvironmentalEffects,
#         on_delete=models.CASCADE
#     )
#     plant_dimensions = models.OneToOneField(
#         PlanDimensions,
#         on_delete=models.CASCADE
#     )
#     harvesting_care = models.OneToOneField(
#         HarvestingCare,
#         on_delete=models.CASCADE
#     )
#     soil_requirements = models.OneToOneField(
#         SoilRequirements,
#         on_delete=models.CASCADE
#     )
#     how_to_plant = models.OneToOneField(
#         HowToPlant,
#         on_delete=models.CASCADE
#     )
#     user_info = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
