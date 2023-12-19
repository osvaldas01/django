from django.urls import path

from .views import index, country

urlpatterns = [
    path("", index, name="country"),
    path('<int:country_id>/', country, name="countries")
]