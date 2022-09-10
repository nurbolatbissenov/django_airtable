from django.db import models

class CityArrive(models.Model):
    city_arr = models.CharField('Arrivals', max_length=100)

    def __str__(self):
        return self.city_arr
