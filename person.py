from abc import ABC
from account import Account

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account
    
    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}, Email: {self.__email}, Phone: {self.__phone}"

class Guest(Person):
    def __init__(self, name, address, email, phone, account):
        super().__init__(name, address, email, phone, account)
        self.__total_rooms_checked_in = 0

class Receptionist(Person):
    def search_member(self, name):
        None
    
    def create_booking(self):
        None

class Server(Person):
    def add_room_charge(self, room, room_charge):
        None
