from models import Tour, Team
from rest_framework import serializers


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['id', 'name', 'description', 'parent', 'active', 'image', 'descendant_ids']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']
