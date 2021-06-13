import django_filters
from django_filters import CharFilter
from .models import *


class PlantFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'name',lookup_expr =      'icontains',label='search plantation items')

    class Meta:
        model = Plant
        fields = ['name']
