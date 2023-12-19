from django.http import HttpResponse
from django.shortcuts import render
from .models import Country, City


def index(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'country/countries.html', context)

def country(request, country_id):
    return HttpResponse(country_id)