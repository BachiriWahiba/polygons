from rest_framework import serializers
from .models import Provider , ServiceArea

class ProviderSerializer(serializers.ModelSerializer):
    """ Provider Serializer  """
    class Meta:
        model = Provider
        fields = '__all__'
        read_only_fields = ('id','created_at','modified_at')

class ServiceAreaSerializer(serializers.ModelSerializer):
    """Service Area Serializer  """

    provider_name = serializers.CharField(read_only = True ,allow_null=True, source ='provider.provider_name')
    
    class Meta:
        model = ServiceArea
        fields = '__all__'
        read_only_fields = ('id','created_at','modified_at')