class Room:
    def __init__(self,name,description,north=None,south=None,west=None,east=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    def get_description(self):
        return self.description


