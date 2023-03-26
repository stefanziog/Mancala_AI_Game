
from MonteCarlo import  AI_Player

ai_player = AI_Player()
class Kalaha:

    def __init__(self, board=None, current_player=0):
        if board is None:
            self.board = [4] * 6 + [0] + [4] * 6 + [0]
        else:
            self.board = board
        self.current_player = current_player

    def copy(self):
        return Kalaha(self.board.copy(), self.current_player)

    # Get move from human player or AI
    def get_move(self):
        if self.current_player == 0:
            move = int(input("Player 0, choose a move: "))
        else:
            move = ai_player.get_move(self)
        return move

    def get_current_player(self):
        return self.current_player

    # Check for winner
    def get_winner(self):
        player0_score = self.board[6]
        player1_score = self.board[13]
        if player0_score == player1_score:
            return None
        elif player0_score > player1_score:
            return 0
        else:
            return 1

    def get_score(self, player):
        if sum(self.board[7:13]) == 0 and self.board[6] > self.board[13] and sum(
                self.board[0:6]) > 0 and self.current_player == 0:
            return self.board[6] + sum(self.board[0:6]) + self.board[13]
        elif sum(self.board[0:6]) == 0 and self.board[13] > self.board[6] and sum(
                self.board[7:13]) > 0 and self.current_player == 1:
            return self.board[13] + sum(self.board[7:13]) + self.board[6]
        elif sum(self.board[0:6]) == 0 and self.current_player == 0:
            return self.board[6] + sum(self.board[7:13])
        elif sum(self.board[7:13]) == 0 and self.current_player == 1:
            return self.board[13] + sum(self.board[0:6])

    # Check for score
    # def get_score(self, player):
    # if sum(self.board[7:13]) == 0 and self.board[6] > self.board[13] and sum(
    # self.board[0:6]) > 0 and self.current_player == 0:
    # return self.board[6] + sum(self.board[0:6])
    # elif sum(self.board[0:6]) == 0 and self.board[13] > self.board[6] and sum(
    # self.board[7:13]) > 0 and self.current_player == 1:
    # return self.board[13] + sum(self.board[7:13])
    # elif sum(self.board[0:6]) == 0 and self.current_player == 0:
    # return self.board[6]
    # elif sum(self.board[7:13]) == 0 and self.current_player == 1:
    # return self.board[13]

    def is_game_over(self):
        return sum(self.board[0:6]) == 0 or sum(self.board[7:13]) == 0

    def get_possible_moves(self):
        if self.current_player == 0:
            return [i for i in range(6) if self.board[i] > 0]
        else:
            return [i for i in range(7, 13) if self.board[i] > 0]

    def get_valid_moves(self):
        if self.current_player == 0:
            return [i for i in range(6) if self.board[i] != 0]
        else:
            return [i for i in range(7, 13) if self.board[i] != 0]

    # Playing game rules
    def play(self, move):
        if move not in self.get_valid_moves():
            return False
        if self.current_player == 0:
            if self.board[move] == 0:
                return False
            stones = self.board[move]
            self.board[move] = 0
            index = move
            while stones > 0:
                index += 1
                if index == 14:
                    index = 0
                if index == 6 and self.current_player == 1:
                    index += 1
                if index == 13 and self.current_player == 0:
                    index = 0
                self.board[index] += 1
                stones -= 1
            if index == 6:
                return True
            if index < 6 and self.board[index] == 1 and self.board[12 - index] > 0:
                self.board[6] += self.board[12 - index] + 1
                self.board[12 - index] = 0
                self.board[index] = 0

            self.current_player = 1
            return True
        else:
            if self.board[move] == 0:
                return False
            stones = self.board[move]
            self.board[move] = 0
            index = move
            while stones > 0:
                index += 1
                if index == 14:
                    index = 0
                if index == 6 and self.current_player == 1:
                    index += 1
                if index == 13 and self.current_player == 0:
                    index = 0
                self.board[index] += 1
                stones -= 1
            if index == 13:
                return True
            if index > 6 and self.board[index] == 1 and self.board[12 - index] > 0:
                self.board[13] += self.board[12 - index] + 1
                self.board[12 - index] = 0
                self.board[index] = 0

            self.current_player = 0
            return True








