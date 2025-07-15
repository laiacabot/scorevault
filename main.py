from player import Player
from game import Game
def main():
    print("Welcome to ScoreVault!")
    print("Track and discover who wins the most across multiple videogames in your family.")

def ask_games():
    games: list[Game] = []
    other_games: bool

    print("Please enter the names of the games")

    other_games = True

    while other_games:
        game_name = input("Please enter game name (or type 'done' to finish): ")
        if game_name.lower() == 'done':
            other_games = False
        else:
            game_difficulty: int = input("Enter game difficulty ")
            new_game = Game(name=game_name, difficulty=game_difficulty)
            games.append(new_game)
            print("We have added a new a new game !!!"+ str(new_game))

    for game in games:
        print(str(game))
    return games


def ask_players(games: list[Game]):
    
    players: list[Player] = []
    other_players: bool

    print("Please enter the names of the players")

    other_players = True
    
    while other_players:
        player_name = input("Please enter player name (or type 'done' to finish): ")                                                                                          
        
        if player_name.lower() == 'done':
            other_players = False
        else: 
            player_lastname = input("Enter player lastname: ")
            player_age: int = input("Enter player age: ")
            
            for game in games:
                print(str(game))


            new_player = Player(name=player_name, lastname=player_lastname, player_age=player_age)
            players.append(new_player) 

            print(new_player.age)


            print("We have created a new player !!! " + str(new_player))   
    

    print(players)
    return players


def ask_wins(players):
    wins: list[int] = []
    for player in players:

        number_of_wins = input("Enter the number of wins for " + player + ": ")
        wins.append(number_of_wins)

    print(wins)
    return wins


def indentify_winner(wins):

    highest_score: int = 0
    winner_index: int = 0
    for i in range(len(wins)):
        if int(wins[i]) > highest_score:
            winner_index = i
            highest_score = int(wins[i])
    return winner_index
   
     



if __name__ == "__main__":
    main()
    players: list[Player] = []
    games: list[Game] = []
    games = ask_games()
    players = ask_players(games)
    wins = ask_wins(players)
    pos = indentify_winner(wins)
    print("the winner is " + players[pos])