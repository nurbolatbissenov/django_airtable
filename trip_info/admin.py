from django.contrib import admin

from trip_info.models import Departures, CityDeparte, CityArrive, Status


class AirportAdmin(admin.ModelAdmin):
    list_display = ('flight',
                    'plane',
                    'city_departure',
                    'schedule_dep',
                    'city_arrive',
                    'schedule_arr',
                    'status'
                    )
    search_fields = ('flight',
                     'plane',
                     'status'
                     )


admin.site.register(Departures, AirportAdmin)
admin.site.register(CityDeparte)
admin.site.register(CityArrive)
admin.site.register(Status)
