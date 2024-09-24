from datetime import datetime
from enum import Enum

class BookingStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CHECKED_OUT, CANCELLED, ABANDONED = 1, 2, 3, 4, 5, 6, 7

class RoomBooking:
    def __init__(self, reservation_number, start_date, duration_in_days, booking_status):
        self.__reservation_number = reservation_number
        self.__start_date = start_date
        self.__duration_in_days = duration_in_days
        self.__status = booking_status
        self.__checkin = None
        self.__checkout = None
        self.__guest_id = 0
        self.__room = None
        self.__invoice = None
        self.__notifications = []
    
    def fetch_details(self, reservation_number):
        None
    
    def __str__(self):
        return f"Reservation #{self.__reservation_number}, Start: {self.__start_date}, Duration: {self.__duration_in_days} days, Status: {self.__status.name}"
