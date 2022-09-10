from django.db import models

class CityDeparte(models.Model):
    city_dep = models.CharField('Departures', max_length=100)

    def __str__(self):
        return self.city_dep
