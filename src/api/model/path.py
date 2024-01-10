from src.api.model.step import Step


class Path:
    def __init__(self, start_coordinates: dict, start_address: str, end_coordinates: dict, end_address: str,
                 duration: int, distance: int, steps: list[Step]):
        self.start_coordinates = start_coordinates
        self.start_address = start_address
        self.end_coordinates = end_coordinates
        self.end_address = end_address
        self.duration = duration
        self.distance = distance
        self.steps = steps

    def serialize(self):
        return {
            "start_coordinates": self.start_coordinates,
            "start_address": self.start_address,
            "end_coordinates": self.end_coordinates,
            "end_address": self.end_address,
            "distance": self.distance,
            "duration": self.duration,
            "steps": self.steps
        }
