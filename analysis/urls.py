# analysis/urls.py

from rest_framework.routers import DefaultRouter
from analysis.views import CompanyViewSet, IndicatorViewSet

from django.urls import path
from analysis import views

urlpatterns = [
    path('companies/', views.CompanyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('chatbot/', views.chatbot_interaction),
]


router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'indicators', IndicatorViewSet, basename='indicator')

urlpatterns_api = router.urls
