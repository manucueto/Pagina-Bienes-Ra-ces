from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from houses import views
from houses.views import massive_create

router = routers.DefaultRouter()
router.register(r'houses', views.HouseViewSet, 'houses')
router.register(r'sellers', views.SellerViewSet, 'sellers')
router.register(r'houses_sellers', views.HouseSellerViewSet, 'houses_sellers')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Bienes Raices API')),
    path('massive/', massive_create, name='massive-create'),
]