from rest_framework import serializers
from . import models as api_models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Movie
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Reservation
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Guest
        fields = ["pk", "reservation", "name", "mobile"]
        # uuid, slug
