
from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import   ProviderViewset, ServiceAreaViewset,EntrypointPolygonAPIview




urlpatterns = [
path('EntryPointPolygon/<str:latitude>/<str:longitude>/', EntrypointPolygonAPIview.as_view()),

]

router = SimpleRouter()

router.register('Provider',ProviderViewset , basename='provider')
router.register('ServiceArea',ServiceAreaViewset , basename='sericeArea')


urlpatterns += router.urls 