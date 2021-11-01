from rest_framework import viewsets

from management.models import Vehicle
from management.serializers.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicle.objects.all().order_by('vid')
    serializer_class = VehicleSerializer
