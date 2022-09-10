from django.urls import path

from trip_info.view.TripApiView import TripApiView
from trip_info.view.views import TripView

urlpatterns = [
    path('', TripView.as_view()),
    path('api/v1/', TripApiView.as_view()),
    path('api/v1/<int:pk>/', TripApiView.as_view()),
]