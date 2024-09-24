from address import Address
from account import Account
from booking import RoomBooking, BookingStatus
from room import Room, RoomStyle, RoomStatus
from person import Guest

from datetime import datetime

# Initialize address
address = Address("65-J1 wapda town", "Lahore", "LR", "54000", "Pakistan")

# Initialize account
guest_account = Account("ahsan", "password123")

# Initialize guest
guest = Guest("makaram", address, "makaram@gmail.com", "0300-0000000", guest_account)

# Initialize room
room = Room(1, RoomStyle.STANDARD, RoomStatus.RESERVED, 89.85, False)

# Initialize booking
booking = RoomBooking("0000011111", datetime(2024, 8, 22), 2, BookingStatus.CONFIRMED)

# Print initialized data
print(guest)
print(room)
print(booking)
