from rest_framework import routers
from .api import PropertyViewSet

router = routers.DefaultRouter()
router.register('api/property', PropertyViewSet, 'property')

urlpatterns = router.urls