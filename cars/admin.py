from django.contrib import admin
from cars.models import Car, Manufacturer

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
