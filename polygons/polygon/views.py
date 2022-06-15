from django.shortcuts import render
from rest_framework import viewsets
from .models import Provider , ServiceArea
from .serializers import ProviderSerializer , ServiceAreaSerializer
# from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ProviderViewset(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

class ServiceAreaViewset(viewsets.ModelViewSet):
    # filter_backends = (DjangoFilterBackend) 
    # filter_fields = {
    #     'geoinformation__lattitude': ['exact', 'gte','lte'],
    #     'geoinformation__long': ['exact', 'gte','lte'],

    # }
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

