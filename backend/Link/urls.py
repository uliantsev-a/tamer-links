"""PlacePass URL Configuration

"""
from rest_framework.routers import DefaultRouter

from .views import LinkViewSet

router = DefaultRouter()
router.register('link', LinkViewSet, base_name='link')

urlpatterns = router.urls
