from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets

from . import models as tickets_models
from . import serializers as tickets_serializers


# Create your views here.
# =================================================================
# 1- without rest and no model query fbv
def no_rest_no_model(request):
    guest = [
        {"id": 1, "name": "mazen", "mobile": "011223334444"},
        {"id": 2, "name": "ali", "mobile": "011223334444"},
    ]
    return JsonResponse(guest, safe=False)


# =================================================================
# 2- no_rest_fram_model
def no_rest_fram_model(request):
    data = tickets_models.Guest.objects.all()
    response = {"guests": list(data.values("name", "mobile"))}
    return JsonResponse(response)


# =================================================================
# list == get
# crearte == post
# pk query == get
# update == put
# detele destroy == delete


# 3- function based viiews
# 3.1 Get Post
@api_view(["GET", "POST"])
def FBV_List(request):
    # GET
    if request.method == "GET":
        guests = tickets_models.Guest.objects.all()
        serializers = tickets_serializers.GuestSerializer(guests, many=True)
        return Response(serializers.data)

    # POST
    elif request.method == "POST":
        serializers = tickets_serializers.GuestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


# =================================================================
# 3.2 Get put delete
@api_view(["GET", "PUT", "DELETE"])
def FBV_pk(request, pk):
    try:
        guest = tickets_models.Guest.objects.get(pk=pk)
    except tickets_models.Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == "GET":
        serializers = tickets_serializers.GuestSerializer(guest)
        return Response(serializers.data)

    # PUT
    elif request.method == "PUT":
        serializers = tickets_serializers.GuestSerializer(guest, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    if request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =================================================================
# CBV Class Based Views
# 4.1 List and Create == GET and Post
class CBV_List(APIView):
    # GET
    def get(self, request, *args, **kwargs):
        guests = tickets_models.Guest.objects.all()
        serializer = tickets_serializers.GuestSerializer(guests, many=True)
        return Response(serializer.data)

    # POST
    def post(self, request, *args, **kwargs):
        serializer = tickets_serializers.GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# CBV Class Based Views
# 4.1 List and Create == GET and Put and delete
class CBV_pk(APIView):
    # GET
    def get_object(self, pk):
        try:
            return tickets_models.Guest.objects.get(pk=pk)
        except tickets_models.Guest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = tickets_serializers.GuestSerializer(guest)
        return Response(serializer.data)

    # put
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = tickets_serializers.GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =================================================================
# 5 mixins
# 5.1 mixins list
class mixins_list(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = tickets_models.Guest.objects.all()
    serializer_class = tickets_serializers.GuestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# 5.2 mixins (get - put - delete)
class mixins_pk(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = tickets_models.Guest.objects.all()
    serializer_class = tickets_serializers.GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


# =================================================================
# 6 Generics
# 6.1 get and post
class generics_list(generics.ListCreateAPIView):
    queryset = tickets_models.Guest.objects.all()
    serializer_class = tickets_serializers.GuestSerializer


# 6.2 (get - put - delete)
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = tickets_models.Guest.objects.all()
    serializer_class = tickets_serializers.GuestSerializer


# =================================================================
# 7 viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = tickets_models.Guest.objects.all()
    serializer_class = tickets_serializers.GuestSerializer


class viewsets_movie(viewsets.ModelViewSet):
    queryset = tickets_models.Movie.objects.all()
    serializer_class = tickets_serializers.MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ["movie"]


class viewsets_reservation(viewsets.ModelViewSet):
    queryset = tickets_models.Reservation.objects.all()
    serializer_class = tickets_serializers.ReservationSerializer


# =================================================================
# 8 find movie
# search movie ->
@api_view(["GET"])
def find_movie(request):
    movies = tickets_models.Movie.objects.filter(
        hall=request.data["hall"],
        movie=request.data["movie"],
    )
    serializer = tickets_serializers.MovieSerializer(movies, many=True)
    return Response(serializer.data)


# =================================================================
# 9 create new reservation
@api_view(["POST"])
def new_reservation(request):
    movie = tickets_models.Movie.objects.get(
        hall=request.data["hall"],
        movie=request.data["movie"],
    )
    guest = tickets_models.Guest()
    guest.name = request.data["name"]
    guest.mobile = request.data["mobile"]
    guest.save()

    reservation = tickets_models.Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)
