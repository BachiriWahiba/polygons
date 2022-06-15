
from rest_framework.routers import SimpleRouter

from .views import   ProviderViewset, ServiceAreaViewset

urlpatterns = []

router = SimpleRouter()

router.register('Provider',ProviderViewset , basename='Provider')
router.register('ServiceArea',ServiceAreaViewset , basename='SericeArea')


urlpatterns += router.urls 