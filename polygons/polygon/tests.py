from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Provider
from .serializers import ProviderSerializer

# Create your tests here.

# initialize the APIClient app
client = Client()

class GetAllProviderTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Provider.objects.create(provider_name="Comercio" ,email="comercio@str.en" ,phone_number="+3312457896", language="english" ,currency="USD")
        Provider.objects.create(provider_name="MetroM" ,email="MetroM@str.ar" ,phone_number="+3312457891", language="arabic" ,currency="euro")
        Provider.objects.create(provider_name="maystroDeliv" ,email="maystroDeliv@str.sp" ,phone_number="+3312457892", language="spanish" ,currency="euro")
    

    def test_get_all_providers(self):
        # get API response
        response = client.get(reverse('Provider'))
        # get data from db
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)