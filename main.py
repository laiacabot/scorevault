def main():
    print("Welcome to ScoreVault!")
    print("Track and discover who wins the most across multiple videogames in your family.")



def ask_players():
    
    players: list[str] = []
    other_players: bool

    print("Please enter the names of the players")

    other_players = True
    
    while other_players:
        new_player = input("Enter player name (or type 'done' to finish): ")
        if new_player.lower() == 'done':
            other_players = False
        else: players.append(new_player)    

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
    players = ask_players()
    wins = ask_wins(players)
    pos = indentify_winner(wins)
    print("the winner is " + players[pos])