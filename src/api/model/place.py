class Place:
    def __init__(self, coordinates: dict, name: str, address: str):
        self.coordinates = coordinates
        self.name = name
        self.address = address

    def serialize(self):
        return {
            "name": self.name,
            "address": self.address,
            "coordinates": self.coordinates
        }
