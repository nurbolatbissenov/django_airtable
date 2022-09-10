from django.shortcuts import render
from django.views.generic import ListView

from trip_info.models import Departures


class TripView(ListView):
    model = Departures
    template_name = 'trip_info/main.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
