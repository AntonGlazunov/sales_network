from rest_framework.routers import DefaultRouter

from sales.apps import SalesConfig
from sales.views import FactoryViewSet, RetailViewSet, IEViewSet

app_name = SalesConfig.name

router = DefaultRouter()
router.register(r'factory', FactoryViewSet, basename='factory')
router.register(r'retail', RetailViewSet, basename='retail')
router.register(r'ie', IEViewSet, basename='ie')

urlpatterns = [
] + router.urls