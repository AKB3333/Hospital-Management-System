from abc import ABC
from datetime import date

class RoomCharge(ABC):
    def __init__(self):
        self.__issue_at = date.today()
    
    def add_invoice_item(self, invoice):
        None

class Amenity(RoomCharge):
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

class RoomService(RoomCharge):
    def __init__(self, is_chargeable, request_time):
        self.__is_chargeable = is_chargeable
        self.__request_time = request_time

class KitchenService(RoomCharge):
    def __init__(self, description):
        self.__description = description
