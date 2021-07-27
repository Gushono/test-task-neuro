class Situation:
    def __init__(self, id: str, description: str) -> None:
        self.id = id
        self.description = description

    def to_json(self) -> dict:
        return {"situation": {"id": self.id, "description": self.description}}
