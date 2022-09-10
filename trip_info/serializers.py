from rest_framework import serializers

from trip_info.models import Departures


class Departure(serializers.ModelSerializer):
    class Meta:
        model = Departures
        fields = ("flight",
                  "plane",
                  "city_departure",
                  "schedule_dep",
                  "city_arrive",
                  "schedule_arr",
                  "status"
                  )
