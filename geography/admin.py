from django.contrib import admin
from .models import Country, City

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'population']
    search_fields = ['name', 'country__name']

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)