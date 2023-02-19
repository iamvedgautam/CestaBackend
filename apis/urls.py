from django.urls import path
from apis.views import CestaViewSet


urlpatterns = [
    # create cesta
    path('cesta/', CestaViewSet.as_view({'post': 'create', 'get': 'list'})),
    # publish cesta
    # subscribe
]
