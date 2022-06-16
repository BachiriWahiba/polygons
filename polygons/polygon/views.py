from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Provider , ServiceArea
from .serializers import ProviderSerializer , ServiceAreaSerializer



# Create your views here.


class ProviderViewset(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

class ServiceAreaViewset(viewsets.ModelViewSet):

    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

class EntrypointPolygonAPIview(APIView) :

    def get(self , request , latitude , longitude):
        latitude = float(latitude)
        longitude = float(longitude)
        polygons = ServiceArea.objects.filter(geoinformation__latitude__lte=latitude,geoinformation__latitude__gt=longitude,geoinformation__longitude__gte=longitude,geoinformation__longitude__lt=latitude)
        polygons_serializer = ServiceAreaSerializer(polygons,many=True).data
        return Response(polygons_serializer,status=status.HTTP_200_OK)
        
