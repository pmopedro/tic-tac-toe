

class RobotTicTacToePlayer():
    
    def __init__ (slef):
        pass

    def make_move(self, table):
        # x and y represents our play
        x = None
        y = None

        self.resolve(table)




        return (x, y)
    
    def resolve(self, table):
        if hasattr(self, "game_resolved"):
            return self.game_resolved
        else:
            self.build_trees(table, player='X')
    

    def build_trees(self, table, player):
        if self.num_plays_left(table) == 0:
            # self.rate_choice()
            print(table)
            return
        else:
            possible_moves = self.possible_moves(table)     # get all possible moves
            print(possible_moves)
            for play in possible_moves:                     # for each possible move
                (x, y) = play                               # extract play position
                table[x][y] = player                        # play move with the given player
                p = self.change_player(player)              # change player
                self.build_trees(table, p)                  # build tree for the next play with new player


    def change_player(self, player):
        return "O" if player == "X" else "X"


    def possible_moves(self, table):
        possible_move = []
        for x in range(3):
            for y in range(3):
                if table[x][y]=='-':
                    possible_move.append([x,y])
        return possible_move
        
    def rate_choice(self):
        pass

    def num_plays_left(self, table):
        return sum('-' in s for s in table)
    

            

r = RobotTicTacToePlayer()
r.build_trees([['-', '-', 'O'], ['-', '-', '-'], ['-', '-', '-']], "X")