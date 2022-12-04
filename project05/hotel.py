from project05.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room_by_number(room_number)
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        people = room.guests
        result = room.free_room
        if not result:
            self.guests -= people

    def status(self):
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        status = f'Hotel {self.name} has {self.guests} total guests' + "\n" + \
                 f'Free rooms: {", ".join(free_rooms)}' + "\n" + \
                 f'Taken rooms: {", ".join(taken_rooms)}'
        return status

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None
