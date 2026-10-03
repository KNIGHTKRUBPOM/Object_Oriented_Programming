class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True

    def __str__(self):
        status = "ว่าง" if self.is_available else "ไม่ว่าง"
        return f"ห้อง {self.room_number} ({self.room_type}) - {status}"
    
class Hotel:
    def __init__(self,):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_in(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                room.is_available = False
                print(f"Check-in ห้อง {room_number} สำเร็จ")
                return
        print(f"ห้อง {room_number} ไม่สามารถ Check-in ได้")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_available:
                room.is_available = True
                print(f"Check-out ห้อง {room_number} สำเร็จ")
                return
        print(f"ห้อง {room_number} ไม่สามารถ Check-out ได้")
    
    def show_rooms(self):
        for room in self.rooms:
            print(room)

hotel = Hotel()
room1 = Room(101, "Standard")
room2 = Room(102, "Deluxe")

hotel.add_room(room1)
hotel.add_room(room2)

hotel.show_rooms()
hotel.check_in(101)
hotel.show_rooms()
hotel.check_out(101)
hotel.show_rooms()