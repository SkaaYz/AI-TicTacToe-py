# Imports
import math
from tabulate import tabulate


# Gameplay class
class Gameplay:
    # Construct (init)
    def __init__(self):
        self.current_mark = "X"
        self.buttons_clicked = []
        self.actual_board = []
        self.current_try = 0
        self.game_win = False
        self.game_running = False

        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.actual_board.append(row)

    # Button Click func
    def Button_Click(self, button_id, buttons_array):
        if buttons_array[button_id - 1] in self.buttons_clicked:
            pass
        else:
            # To get the actual row of the clicked button, I just divide it by 3, for the row I just use a modulo 3,
            # so I instantly get the right row. (need to math.ceil because values are often like 0.3333333)
            row = (button_id - 1) % 3
            col = math.ceil(button_id / 3)

            # Add the clicked button object to the array (list) and change the current text by the current mark instead
            buttons_array[button_id - 1].configure(text=self.current_mark)
            self.buttons_clicked.append(buttons_array[button_id - 1])

            # Add the current mark to the "actual board" array
            self.actual_board[col - 1][row] = self.current_mark

            # Increment the actual tries var
            self.current_try = self.current_try + 1

            # Test
            if self.Win_Check(self.current_mark):
                print("won!")
            else:
                print("not won")

            # Know if it's actually X or O by using a modulo
            if self.current_try % 2 == 0:
                self.current_mark = "X"
            else:
                self.current_mark = "O"

    # Check if there's a winner (Credits: GeekFlare.com)
    def Win_Check(self, current_mark):
        # Get actual length of the game board
        n = len(self.actual_board)

        # Check rows
        for i in range(n):
            self.game_win = True
            for j in range(n):
                if self.actual_board[i][j] != current_mark:
                    self.game_win = False
                    break
            if self.game_win:
                self.game_running = False
                return self.game_win

        # Check columns
        for i in range(n):
            self.game_win = True
            for j in range(n):
                if self.actual_board[j][i] != current_mark:
                    self.game_win = False
                    break
            if self.game_win:
                self.game_running = False
                return self.game_win

        # Check diagonals
        self.game_win = True
        for i in range(n):
            if self.actual_board[i][i] != current_mark:
                self.game_win = False
                break
        if self.game_win:
            self.game_running = False
            return self.game_win

        # Check "reversed" rows, columns & diagonals
        self.game_win = True
        for i in range(n):
            if self.actual_board[i][n - 1 - i] != current_mark:
                self.game_win = False
                break
        if self.game_win:
            self.game_running = False
            return self.game_win

        # Check for tie
        self.game_win = False
        if self.current_try >= 9:
            print("tie :/")
            self.game_running = False
            return self.game_win
