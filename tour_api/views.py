from rest_framework import viewsets

from models import Tour, Team
from tour_api.serializers import TourSerializer, TeamSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.all
    serializer_class = TourSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.all
    serializer_class = TeamSerializer
