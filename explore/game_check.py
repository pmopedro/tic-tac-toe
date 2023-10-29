class GameCheck():

    def check_win(self, table, player):
        # vertical check
        for x_index, col in enumerate(table):
            win = True
            pattern_list = []
            for y_index, content in enumerate(col):
                if content != player:
                    win = False
                    break
                else:
                    pattern_list.append((x_index, y_index))
            if win is True:
                return player

        # horizontal check
        for row in range(len(table)):
            win = True
            pattern_list = []
            for col in range(len(table)):
                if table[col][row] != player:
                    win = False
                    break
                else:
                    pattern_list.append((col, row))
            if win is True:
                return player

        # left diagonal check
        for index, row in enumerate(table):
            win = True
            if row[index] != player:
                win = False
                break
        if win is True:
            return player

        # right diagonal check
        for index, row in enumerate(table[::-1]):
            win = True
            if row[index] != player:
                win = False
                break
        if win is True:
            return player

        # blank table cells check
        blank_cells = 0
        for row in table:
            for cell in row:
                if cell == "-":
                    blank_cells += 1
        if blank_cells == 0:
            pass

    def game_check(self, table, player):
        win = self.check_win(table, player)
        loose = self.check_win(table, self.change_player(player))

        if win:
            return win
        elif loose:
            return loose
        else:
            return None
