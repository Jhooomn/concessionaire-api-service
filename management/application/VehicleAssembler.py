from management.models import Vehicle
import json
from random import randrange


class VehicleAssembler:
    def __init__(self):
        pass

    @staticmethod
    def get_json(json_string):
        try:
            if json_string:
                return json.loads(json.dumps(json_string))
            return None
        except Exception as e:
            print("There was an error --> {}".format(e))

    @staticmethod
    def json_to_dto(json_string):
        json_model = VehicleAssembler.get_json(json_string)
        if json_model:
            vehicle = Vehicle()
            vehicle.vid = randrange(1000)
            vehicle.type = json_string["type"]
            vehicle.brand = json_string["brand"]
            vehicle.model = json_string["model"]
            vehicle.version = json_string["version"]
            vehicle.licensePlate = json_string["licensePlate"]
            vehicle.km = json_string["km"]
            vehicle.imgLink = json_string["imgLink"]
            return vehicle
        else:
            return None

    @staticmethod
    def json_to_dto_update(json_string):
        json_model = VehicleAssembler.get_json(json_string)
        if json_model:
            vehicle = Vehicle()
            vehicle.vid = int(json_string["vid"])
            vehicle.type = json_string["type"]
            vehicle.brand = json_string["brand"]
            vehicle.model = json_string["model"]
            vehicle.version = json_string["version"]
            vehicle.licensePlate = json_string["licensePlate"]
            vehicle.km = json_string["km"]
            vehicle.imgLink = json_string["imgLink"]
            print(str(vehicle.vid) + vehicle.type + vehicle.brand + vehicle.model + vehicle.version
                  + vehicle.licensePlate + vehicle.km + vehicle.imgLink)
            return vehicle
        else:
            return None

    @staticmethod
    def data_trasnfer(vehicle_from_, vehicle_to_):
        vehicle_to_.vid = vehicle_from_.vid
        vehicle_to_.type = vehicle_from_.type
        vehicle_to_.brand = vehicle_from_.brand
        vehicle_to_.model = vehicle_from_.model
        vehicle_to_.version = vehicle_from_.version
        vehicle_to_.licensePlate = vehicle_from_.licensePlate
        vehicle_to_.km = vehicle_from_.km
        vehicle_to_.imgLink = vehicle_from_.imgLink
        return vehicle_to_

    @staticmethod
    def query_model_to_map(query_model):
        if query_model is not None:
            return {
                'vid': query_model.vid,
                'type': query_model.type,
                'model': query_model.model,
                'version': query_model.version,
                'licensePlate': query_model.licensePlate,
                'km': query_model.km,
                'imgLink': query_model.imgLink,
                'brand': query_model.brand
            }
        return {
            'vid': None,
            'type': None,
            'model': None,
            'version': None,
            'licensePlate': None,
            'km': None,
            'imgLink': None,
            'brand': None
        }
