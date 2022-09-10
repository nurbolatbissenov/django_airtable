from django.db import models
from trip_info.models import CityDeparte, CityArrive, Status


class Departures(models.Model):
    flight = models.CharField('Flight', max_length=100)
    plane = models.CharField('Plane', max_length=100)
    city_departure = models.ForeignKey(CityDeparte, max_length=100, unique=False, on_delete=models.CASCADE)
    schedule_dep = models.CharField('Schedule Departure', max_length=50)
    city_arrive = models.ForeignKey(CityArrive, max_length=100, unique=False, on_delete=models.CASCADE)
    schedule_arr = models.CharField('Schedule Arrivals', max_length=50)
    status = models.ForeignKey(Status, max_length=50, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.flight