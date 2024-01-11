class Step:
    def __init__(self, start_coordinates: dict, end_coordinates: dict, distance: int, duration: int, instruction: str):
        self.start_coordinates = start_coordinates
        self.end_coordinates = end_coordinates
        self.distance = distance
        self.duration = duration
        self.instruction = instruction

    def serialize(self):
        return {
            "start_coordinates": self.start_coordinates,
            "end_coordinates": self.end_coordinates,
            "distance": self.distance,
            "duration": self.duration,
            "instruction": self.instruction
        }
