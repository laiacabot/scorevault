class Game:
    def __init__(self, name: str, difficulty: int):
        self.name = name
        self.difficulty = difficulty


    def __str__(self):
        return f"{self.name} (Difficulty: {self.difficulty})"
    

