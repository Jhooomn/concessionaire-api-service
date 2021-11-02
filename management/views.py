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
    print("validate")
    if vehicle is not None:
        try:
            print("not null")
            vehicle.save()
            print("it saved")
        except:
            print("error")
            pass
    else:
        print("is none")
        return Response([], status=status.HTTP_200_OK)
    print("will return")
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
    db_vehicle = Vehicle.objects.get(id=vehicle.vid)
    if db_vehicle is not None:
        db_vehicle = VehicleAssembler.data_trasnfer(vehicle, db_vehicle)
        db_vehicle.update_or_create()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_409_CONFLICT)


@api_view(['DELETE'])
def delete(request, id):
    print("to delete {}".format(id))
    employee = Vehicle.objects.get(id=id)
    employee.delete()
