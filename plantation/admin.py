from django.contrib import admin
from .models import Plant
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Plant)

