from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from trip_info.models import Departures
from trip_info.serializers import Departure


class TripApiView(APIView):
    def get(self, request):
        trip = Departures.objects.all()
        return Response({'post': Departure(trip, many=True).data})

    def post(self, request):
        serializer = Departure(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put not allowed"})

        try:
            instance = Departures.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        serializer = Departure(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put not allowed"})
        try:
            instance = Departures.objects.get(pk=pk)
            instance.delete()
            return Response({"post": "Delete post " + str(pk)})
        except:
            return Response({"error": "Objects does not exists"})
