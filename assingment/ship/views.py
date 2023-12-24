from rest_framework import filters, status, viewsets
from .models import Ship, ShipPosition
from .serializers import ShipSerializer, ShipPositionSerialiser


class ShipViewSet(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing ships.
    create:
        Create a new shihp instance.
    retrieve:
        Return the given ship.
    update:
        Update the given ship.
    partial_update:
        Update the given ship given field only.
    destroy:
        Delete the given ship.
    """

    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ShipPositionViewSet(viewsets.ModelViewSet):
    """
    list:
        Return a list of all the existing ships.
    create:
        Create a new shihp instance.
    retrieve:
        Return the given ship.
    update:
        Update the given ship.
    partial_update:
        Update the given ship given field only.
    destroy:
        Delete the given ship.
    """

    queryset = ShipPosition.objects.all()
    serializer_class = ShipPositionSerialiser

    def get_queryset(self):

        queryset = ShipPosition.objects.all()
        imo = self.request.query_params.get('imo')

        if imo:
            queryset = queryset.filter(ship__imo_number=imo)

        return queryset.order_by('-id')
