from django_filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from sales.models import Factory, Retail, IE
from sales.serializers import FactorySerializer, RetailSerializer, IESerializer
from users.permissions import IsAuthenticatedAndActive


class FactoryViewSet(viewsets.ModelViewSet):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticatedAndActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country',]


class RetailViewSet(viewsets.ModelViewSet):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticatedAndActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country', ]


class IEViewSet(viewsets.ModelViewSet):
    serializer_class = IESerializer
    queryset = IE.objects.all()
    permission_classes = [IsAuthenticatedAndActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country', ]
