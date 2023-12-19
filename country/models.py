from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=30)
    pub_date = models.CharField(max_length=50)
    population = models.IntegerField(default=0)
    continent = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.country}, {self.continent}, {self.population}'

class City(models.Model):
    city = models.CharField(max_length=30)
    city_population = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}, {self.country.country}'
