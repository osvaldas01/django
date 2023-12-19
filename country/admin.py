from django.contrib import admin
from .models import Country, City
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ["country", "population"]

admin.site.register(Country, CountryAdmin)
admin.site.register(City)