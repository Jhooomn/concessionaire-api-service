from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from management.application.VehicleAssembler import VehicleAssembler
from management.forms import VehicleForm
from management.models import Vehicle
from management.serializers.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicle.objects.all().order_by('vid')
    serializer_class = VehicleSerializer


@api_view(['POST'])
def save(request):
    vehicle = VehicleAssembler.json_to_dto(request.data)
    if vehicle is not None:
        try:
            vehicle.save()
        except:
            pass
    else:
        return Response([], status=status.HTTP_200_OK)
    return Response([], status=status.HTTP_200_OK)


@api_view(['GET'])
def list(request):
    vehicles_response = []
    get_all_vehicles(vehicles_response)
    return Response(vehicles_response, status=status.HTTP_200_OK)


def get_all_vehicles(vehicles_response):
    for vehicle in Vehicle.objects.all():
        vehicles_response.append(VehicleAssembler.query_model_to_map(query_model=vehicle))


@api_view(['PUT'])
def update(request):
    vehicle = VehicleAssembler.json_to_dto_update(request.data)
    db_vehicle = Vehicle.objects.get(licensePlate=vehicle.licensePlate)
    if db_vehicle is not None:
        db_vehicle = VehicleAssembler.data_trasnfer(vehicle, db_vehicle)
        delete_vehicle(vehicle)
        db_vehicle.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_409_CONFLICT)


@api_view(['PUT'])
def delete(request):
    vehicle = VehicleAssembler.json_to_dto(request.data)
    delete_vehicle(vehicle)
    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_vehicle(vehicle):
    vehicles_response = []
    get_all_vehicles(vehicles_response)
    for db_v in vehicles_response:
        if vehicle.vid == db_v["vid"]:
            vehicle = VehicleAssembler.json_to_dto_update(db_v)
            vehicle.delete()
            break
