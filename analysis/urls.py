# analysis/urls.py

from rest_framework.routers import DefaultRouter
from analysis.views import CompanyViewSet, IndicatorViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'indicators', IndicatorViewSet, basename='indicator')

urlpatterns_api = router.urls
