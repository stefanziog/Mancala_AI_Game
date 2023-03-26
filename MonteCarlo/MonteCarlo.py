
import random

class AI_Player:

    def __init__(self, num_simulations=100):
        self.num_simulations = num_simulations

    def get_move(self, game):
        possible_moves = game.get_possible_moves()
        if len(possible_moves) == 1:
            return possible_moves[0]
        else:
            win_rates = []
            for move in possible_moves:
                wins = 0
                for i in range(self.num_simulations):
                    cloned_game = game.copy()
                    cloned_game.play(move)
                    result = self.simulate_random_game(cloned_game)
                    if result == game.get_current_player():
                        wins += 1
                win_rates.append(wins / self.num_simulations)
            best_move_index = win_rates.index(max(win_rates))
            return possible_moves[best_move_index]

    def simulate_random_game(self, game):
        while not game.is_game_over():
            possible_moves = game.get_possible_moves()
            move = random.choice(possible_moves)
            game.play(move)
        return game.get_winner()

