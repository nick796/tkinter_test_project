from Room import Room
class Game:
    def __init__(self):
        self.rooms = {
            "Start": Room("Start","You are in a dark room.",north="Hall",east="MonkLand"),
            "Hall":Room("Hall","You are in a new made hall",south="Start")
        }
        self.current_room = self.rooms["Start"]
    def get_description(self):
        return self.current_room.get_description()

    def get_available_directions(self):
        directions = []
        if self.current_room.north:
            directions.append("north")
        if self.current_room.south:
            directions.append("south")
        if self.current_room.west:
            directions.append("west")
        if self.current_room.east:
            directions.append("east")
        return directions

    def move(self,direction):
        next_room_name = getattr(self.current_room,direction)
        if next_room_name:
            self.current_room = self.rooms[next_room_name]
        else:
            print("You can't go that way.")