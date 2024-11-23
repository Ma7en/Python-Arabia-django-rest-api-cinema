from rest_framework import serializers
from . import models as tickets_models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets_models.Movie
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets_models.Reservation
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets_models.Guest
        fields = ["pk", "reservation", "name", "mobile"]
        # uuid, slug


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets_models.Post
        fields = "__all__"
