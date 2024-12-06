from rest_framework.routers import DefaultRouter
from .views import PlacesViewSet

router = DefaultRouter()
router.register(r'places', PlacesViewSet, basename='places')

urlpatterns = router.urls