

from kalaha import Kalaha
from MonteCarlo import AI_Player


game = Kalaha()
ai_player = AI_Player()

while not game.is_game_over():
    current_player = game.get_current_player()
    print("Current player:", current_player)
    # Format and print the board
    # first row is reversed to have the prospective of the player if he/she was sitting across
    row1 = "      | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[12], game.board[11], game.board[10], game.board[9],
                                                         game.board[8], game.board[7])
    row2 = "| {} |                                  | {} |".format(game.board[13], game.board[6])
    row3 = "       | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[0], game.board[1], game.board[2],game.board[3], game.board[4], game.board[5])
    #row1 = "       | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[5], game.board[4], game.board[3],game.board[2], game.board[1], game.board[0])

    #row3 = "      | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[7], game.board[8], game.board[9], game.board[10],
                                                         #game.board[11], game.board[12])
    print("Board: ", row1, "\n        ", row2, "\n        ", row3)
    #Human player turn or AI_Player turn
    if current_player == 0:
        move = int(input("Player 0, choose a move: "))
    else:

        move = ai_player.get_move(game)
        print("AI chooses move:", move)
    success = game.play(move)
    while not success:
        print("Invalid move, try again.")
        if current_player == 0:
            move = int(input("Player 0, choose a move: "))
        else:
            move = ai_player.get_move(game)
            print("AI chooses move:", move)
        success = game.play(move)

winner = game.get_winner()
if winner is None:
    print("It's a tie!")
else:
    print("Player", winner, "wins with a score of", game.get_score(winner))



"""""
def main():
    # initialize the game and the AI player
    game = Kalaha()
    ai_player = Monte_Carlo(game)  # create Monte_Carlo object with the current game state
    # loop until the game is over
    while not game.is_game_over():
        #print the board
        current_player = game.get_current_player()
        print("Current player:", current_player)
        # Format and print the board
        # first row is reversed to have the prospective of the player if he/she was sitting across
        row1 = "       | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[5], game.board[4], game.board[3],
                                                                    game.board[2], game.board[1], game.board[0])
        row2 = "| {} |                                  | {} |".format(game.board[6], game.board[13])
        row3 = "      | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[7], game.board[8], game.board[9],
                                                                   game.board[10],
                                                                   game.board[11], game.board[12])
        print("Board: ", row1, "\n        ", row2, "\n        ", row3)

        # get the current player
        if game.current_player == 0:
            # get human move
            move = int(input("Enter a move: "))
            while move not in game.get_valid_moves():
                move = int(input("Invalid move. Enter a move: "))
        else:
            # get computer move
            move = ai_player.search(1000)
            print(f"Computer plays move {move}")

        # make move and switch player
        game.play(move)

    # print final board and winner
    print(game)
    winner = game.get_winner()
    if winner is None:
        print("Tie game.")
    else:
        print(f"Player {winner} wins!")

if __name__ == "__main__":
    main()
    """""
