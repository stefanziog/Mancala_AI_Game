from mancala import Kalaha
from minimax import AI_Player


game = Kalaha()



while not game.is_game_over():
    current_player = game.get_current_player()
    print("Current player:", current_player)
    # Format and print the board
    row1 = "       | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[5], game.board[4], game.board[3],game.board[2], game.board[1], game.board[0])
    row2 = "| {} |                                  | {} |".format(game.board[6], game.board[13])
    row3 = "      | {} |  {} |  {} |  {} |  {} |  {} |".format(game.board[7], game.board[8], game.board[9], game.board[10],
                                                         game.board[11], game.board[12])
    print("Board: ", row1, "\n        ", row2, "\n        ", row3)
    if current_player == 0:
        move = int(input("Player 0, choose a move: "))
    else:
        ai_player = AI_Player()
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