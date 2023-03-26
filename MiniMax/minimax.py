import copy
import numpy as np


class AI_Player:
    def __init__(self, max_depth=8):
        self.max_depth = max_depth

    def get_move(self, game):
        move = self.MiniMax(game, self.max_depth, -9999999, 9999999, True)
        return move

    def MiniMax(self, state, depth, alpha, beta, maximizing_player):

        if depth == 0 or state.is_game_over():
            if maximizing_player:
                return 4 * state.get_score(1) - sum(state.board[7:13]) - np.count_nonzero(state.board[7:13]) - (
                            4 * state.get_score(0) - sum(state.board[0:6]) - np.count_nonzero(state.board[0:6]))
            else:
                return 4 * state.get_score(0) - sum(state.board[0:6]) - np.count_nonzero(state.board[0:6]) - (
                            4 * state.get_score(1) - sum(state.board[7:13]) - np.count_nonzero(state.board[7:13]))

        if maximizing_player:
            maxvalue = -9999999
            best_move = None

            for move in state.get_possible_moves():

                game_state_copy = copy.deepcopy(state)
                game_state_copy.play(move)

                value = self.MiniMax(game_state_copy, depth - 1, alpha, beta, False)

                if value > maxvalue:
                    maxvalue = value
                    best_move = move

                alpha = max(alpha, -(4 * game_state_copy.get_score(0) - 4 * game_state_copy.get_score(1) - sum(
                    game_state_copy.board[0:6]) + sum(game_state_copy.board[7:13]) + np.count_nonzero(
                    game_state_copy.board[7:13]) - np.count_nonzero(game_state_copy.board[0:6])))
                if beta <= alpha:
                    break
            if depth == self.max_depth:
                return best_move
            else:
                return maxvalue
        else:
            minvalue = 9999999
            best_move = None

            for move in state.get_possible_moves():

                game_state_copy = copy.deepcopy(state)
                game_state_copy.play(move)

                value = self.MiniMax(game_state_copy, depth - 1, alpha, beta, True)
                if value < minvalue:
                    minvalue = value
                    best_move = move

                beta = min(beta, 4 * game_state_copy.get_score(0) - 4 * game_state_copy.get_score(1) - sum(
                    game_state_copy.board[0:6]) + sum(game_state_copy.board[7:13]) - np.count_nonzero(
                    game_state_copy.board[0:6]) + np.count_nonzero(game_state_copy.board[7:13]))
                if beta <= alpha:
                    break
            if depth == self.max_depth:
                return best_move
            else:
                return minvalue
