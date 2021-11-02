from rest_framework import serializers

from management.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'type', 'brand', 'model', 'version'
                  , 'licensePlate', 'km', 'imgLink')
