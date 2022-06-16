from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer

# Create your tests here.

# initialize the APIClient app
client = Client(enforce_csrf_checks=True)

class ProviderTest(TestCase):
    """ Test Provider API """

    REVERSE_PROVIDER = '/Polygon/Provider/'
    REVERSE_PROVIDER_RETREIVE_DELETE_UPDATE = '/Polygon/Provider/2/'

    def setUp(self):
        Provider.objects.create(provider_name="Comercio" ,email="comercio@str.en" ,phone_number="+3312457896", language="english" ,currency="USD")
        Provider.objects.create(provider_name="MetroM" ,email="MetroM@str.ar" ,phone_number="+3312457891", language="arabic" ,currency="EUR")
        Provider.objects.create(provider_name="maystroDeliv" ,email="maystroDeliv@str.sp" ,phone_number="+3312457892", language="spanish" ,currency="EUR")
    

    def test_get_all_providers(self):
        
        # get API response
        response = client.get(self.REVERSE_PROVIDER)
        # get data from db
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_providers(self):
        
        # get API response
        response = client.post(self.REVERSE_PROVIDER,{"provider_name":"TrainTL" ,"email":"TrainTL@str.sp" ,"phone_number":"+3312457875", "language":"spanish" ,"currency":"EUR"})
        # assert code status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # def test_retreive_provider(self):
    #     # get API response

    #     response = client.get(self.REVERSE_PROVIDER_RETREIVE_DELETE_UPDATE)

    #     response_data = response.data
    #     print("responsedata : ",response.data)
    #     # get data from db
    #     self.assertEqual(response_data["id"], 2)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ServiceAreaTest(TestCase):
    """ Test Service area  API """

    REVERSE_SERVICEAREA = '/Polygon/ServiceArea/'


    def setUp(self):
        provider_2 = Provider.objects.filter(id=2).first()
        provider_3 = Provider.objects.filter(id=3).first()
        provider_4 = Provider.objects.filter(id=3).first()
        ServiceArea.objects.create(service_area_name="Emporia, KS, USA",price=50,provider=provider_2,geoinformation={"latitude":38.405903,"longitude":-96.188339})
        ServiceArea.objects.create(service_area_name="Dodge City, KS, USA",price=40,provider=provider_3,geoinformation={"latitude":37.753098,"longitude":-100.024872})
        ServiceArea.objects.create(service_area_name="Council Grove, KS, USA",price=60,provider=provider_4,geoinformation={"latitude":38.661697,"longitude":-96.492599})
    

    def test_get_service_area(self):
        
        # get API response
        response = client.get(self.REVERSE_SERVICEAREA)
        # get data from db
        service_area = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_area, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_post_service_area(self):
        
    #     # get API response
    #     response = client.post(self.REVERSE_SERVICEAREA,
    #     {
    #         "service_area_name":"MPMO, KLS, USA",
    #         "price":30,
    #         "provider":2,
    #         "geoinformation":{
    #             "latitude":41.563606,
    #             "longitude":-95.125549
    #         }
    #     })
    #     # assert code status
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    


class EntrypointPolygonTest(TestCase):
    """ Test EntrypointPolygon view API """

    def test_entrypoint_polygon(self):
        latitude = 38.705903
        longitude = -100.024872
        reverse_endpoint_polygon = '/Polygon/EntryPointPolygon/38.705903/-100.024872/'
        # get API response
        response = client.get(reverse_endpoint_polygon)
        # get data from db
        polygons = ServiceArea.objects.filter(geoinformation__latitude__lte=latitude,geoinformation__latitude__gt=longitude,geoinformation__longitude__gte=longitude,geoinformation__longitude__lt=latitude)
        serializer = ServiceAreaSerializer(polygons, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   