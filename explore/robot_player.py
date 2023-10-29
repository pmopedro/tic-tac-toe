import copy
import json
from game_check import GameCheck


# class PossibleMove():
#     def __init__(self, move, rate=None):
#         self.move = move
#         self.rate = rate
import time


class RobotTicTacToePlayer(GameCheck):

    def __init__(self, player="O"):
        self.player = player

    def make_move(self, table):
        best_move = self.minimax(
            table, self.player, -float('inf'), float('inf'))
        time.sleep(0.4)
        return best_move

    def build_json(self, table, player, rate=None):
        possible_moves = self.possible_moves(table)
        game_state = self.game_check(table, self.player)

        if game_state is not None:
            # If the game is already over, return the result (1 if bot wins, -1 if bot loses, 0 for a tie).
            if game_state == self.player:
                return 1
            else:
                return -1
        elif len(possible_moves) == 0:
            # It's a tie.
            return 0

        tree_json = []
        for move in possible_moves:
            x, y = move
            new_table = copy.deepcopy(table)
            new_table[x][y] = player
            result = self.build_json(new_table, self.change_player(player))
            tree_json.append({
                "player": player,
                "move": str((x, y)),
                "table": str(new_table),
                "rate": result
            })

        return tree_json

    def minimax(self, table, player, alpha, beta):
        possible_moves = self.possible_moves(table)
        game_state = self.game_check(table, self.player)

        if game_state is not None:
            # If the game is already over, return the result (1 if bot wins, -1 if bot loses, 0 for a tie).
            if game_state == self.player:
                return 1, None
            else:
                return -1, None
        elif len(possible_moves) == 0:
            # It's a tie.
            return 0, None
        best_score = -float('inf') if player == self.player else float('inf')
        best_move = None

        for move in possible_moves:
            x, y = move
            new_table = copy.deepcopy(table)
            new_table[x][y] = player
            score, _ = self.minimax(
                new_table, self.change_player(player), alpha, beta)

            if player == self.player:  # Maximizer (bot's turn)
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if best_score >= beta:
                    break
            else:  # Minimizer (opponent's turn)
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if best_score <= alpha:
                    break

        return best_score, best_move

    def change_player(self, player):
        return "O" if player == "X" else "X"

    def possible_moves(self, table):
        possible_move = []
        for x in range(3):
            for y in range(3):
                if table[x][y] == '-':
                    possible_move.append([x, y])
        return possible_move

    def rate_choice(self):
        pass

    def num_plays_left(self, table):
        return sum('-' in s for s in table)

    def print_table(self, table):
        for i in range(len(table)):
            print(table[i])


# table = [
#     ['O', '-', 'X'],
#     ['X', 'O', '-'],
#     ['X', '-', '-']]

# r = RobotTicTacToePlayer(player="O")
# move = r.make_move(table)
# print(move)
# resp = r.build_json(
#     table,
#     "O")

# print(json.dumps(resp, indent=2))
