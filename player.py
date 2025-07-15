from game import Game

class Player:

    def __init__(self, name: str, lastname: str, player_age:int = 0, game: Game = None):
        """Initialize a Player with name, lastname, age, and preferred game."""
        self.name = name
        self.lastname = lastname
        self.age = player_age
        self.preferred_game = game


    def __str__(self):
        return f"{self.name} {self.lastname} (Age: {self.age})"


