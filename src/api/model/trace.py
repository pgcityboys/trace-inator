from api.model.path import Path


class TraceModel:
    def __init__(self, paths: list[Path]):
        self.paths = paths
