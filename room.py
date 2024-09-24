from enum import Enum
from search import Search

class RoomStyle(Enum):
    STANDARD, DELUXE, FAMILY_SUITE, BUSINESS_SUITE = 1, 2, 3, 4

class RoomStatus(Enum):
    AVAILABLE, RESERVED, OCCUPIED, NOT_AVAILABLE, BEING_SERVICED, OTHER = 1, 2, 3, 4, 5, 6

class Room(Search):
    def __init__(self, room_number, room_style, status, price, is_smoking):
        self.__room_number = room_number
        self.__style = room_style
        self.__status = status
        self.__booking_price = price
        self.__is_smoking = is_smoking
    
    def __str__(self):
        smoking_status = "Smoking" if self.__is_smoking else "Non-Smoking"
        return f"Room {self.__room_number}, Style: {self.__style.name}, Price: ${self.__booking_price}/night, {smoking_status}"
    
    def is_room_available(self):
        None
    
    def check_in(self):
        None
    
    def check_out(self):
        None
    
    def search(self, style, start_date, duration):
        None
