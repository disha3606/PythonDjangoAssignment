from django.contrib import admin

from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dom', 'type', 'locality', 'city', 'pin', 'state', 'mobile', 'car_city', 'profile_image']
