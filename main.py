import random


class Game:
    def __init__(self):
        self.board = ["-", "-", "-",  # 0 first
                      "-", "-", "-",  # 1
                      "-", "-", "-"]  # 2
        #   second      0   1   2
        self.players_turn = 1
        self.game_over = False

    def _piece(self):
        if self.players_turn == 1:
            return "x"
        return "o"

    def _swap_turn(self):
        if self.players_turn == 1:
            self.players_turn = 2
        else:
            self.players_turn = 1

    def turn(self, move):
        # make sure response is valid.
        try:
            move = int(move)
        except ValueError:
            print("ERROR Must enter valid numbers!")
            return
        if move > 9:
            print("ERROR selection must be 1-9!")
            return

        if self.board[move - 1] == "-":
            self.board[move - 1] = self._piece()
            self._swap_turn()
        else:
            # print(self.board[move - 1])
            print("ERROR that space is already occupied!")
            return
        self.print_board()
        self._check_if_game_over()

    def _check_if_game_over(self):
        # row 1
        if self.board[0] == self.board[1] == self.board[2] != "-":
            print(f"Game over result: {self.board[0]} Wins")
            self.game_over = True
        # row 2
        elif self.board[3] == self.board[4] == self.board[5] != "-":
            print(f"Game over result: {self.board[3]} Wins")
            self.game_over = True
        # row 3
        elif self.board[6] == self.board[7] == self.board[8] != "-":
            print(f"Game over result: {self.board[6]} Wins")
            self.game_over = True
        # col 1
        elif self.board[0] == self.board[3] == self.board[6] != "-":
            print(f"Game over result: {self.board[0]} Wins")
            self.game_over = True
        # col 2
        elif self.board[1] == self.board[4] == self.board[7] != "-":
            print(f"Game over result: {self.board[1]} Wins")
            self.game_over = True
        # col 3
        elif self.board[2] == self.board[5] == self.board[8] != "-":
            print(f"Game over result: {self.board[2]} Wins")
            self.game_over = True
        # diag top left to bottom right
        elif self.board[0] == self.board[4] == self.board[8] != "-":
            print(f"Game over result: {self.board[0]} Wins")
            self.game_over = True
        # diag top right to bottom left
        elif self.board[2] == self.board[4] == self.board[6] != "-":
            print(f"Game over result: {self.board[2]} Wins")
            self.game_over = True
        else:
            # if all squares are filled and no winner
            for space in self.board:
                if space == "-":
                    return
            self.game_over = True
            print("Game over result: Cat's game.")

    def print_board(self):
        print()
        board = self.board.copy()
        print("", board[0], board[1], board[2],
              "\n", board[3], board[4], board[5],
              "\n", board[6], board[7], board[8])
        print()

    def bot_turn(self):
        self._swap_turn()
        self.print_board()
        self._check_if_game_over()
# if bot is x
# bot gets max enemy gets min


def check_if_game_over(board):
    # row 1
    if board[0] == board[1] == board[2] != "-":
        return True, board[0]
    # row 2
    elif board[3] == board[4] == board[5] != "-":
        return True, board[3]
    # row 3
    elif board[6] == board[7] == board[8] != "-":
        return True, board[6]
    # col 1
    elif board[0] == board[3] == board[6] != "-":
        return True, board[0]
    # col 2
    elif board[1] == board[4] == board[7] != "-":
        return True, board[1]
    # col 3
    elif board[2] == board[5] == board[8] != "-":
        return True, board[2]
    # diag top left to bottom right
    elif board[0] == board[4] == board[8] != "-":
        return True, board[0]
    # diag top right to bottom left
    elif board[2] == board[4] == board[6] != "-":
        return True, board[2]
    else:
        for space in board:
            if space == "-":
                return False, ""  # game isn't over, this piece doesn't get checked
        return True, "="  # Cat's game


def out_value(piece):
    if piece == "x":
        return 100
    elif piece == "o":
        return -100
    elif piece == "=":
        return 0


def minimax(pos, maximize=True, og=True):
    over, out = check_if_game_over(pos)
    if over:
        return out_value(out)

    space_num = 0
    # this exists to return a move choice rather than the maximized outcome
    if og:
        move_list = []
        for space in pos:
            if space == "-":
                dupe = pos.copy()
                dupe[space_num] = "x"
                eval = minimax(dupe, maximize=False, og=False)
                move_list.append(eval)
            else:
                move_list.append(-100)
            space_num += 1
        space_num = 0
        move_choices = []
        for i in move_list:
            if i == max(move_list):
                move_choices.append(space_num + 1)
            space_num += 1
        print("Choices:", move_choices)
        return max(move_list), random.choice(move_choices)

    if maximize:
        maxEval = -100
        for space in pos:
            if space == "-":
                dupe = pos.copy()
                dupe[space_num] = "x"
                eval = minimax(dupe, maximize=False, og=False)
                maxEval = max(maxEval, eval)
            space_num += 1
        return maxEval

    else:
        minEval = 100
        for space in pos:
            if space == "-":
                dupe = pos.copy()
                dupe[space_num] = "o"
                eval = minimax(dupe, og=False)
                minEval = min(minEval, eval)
            space_num += 1
        return minEval


def outcome(probability):
    if probability == 0:
        return "Tie"
    elif probability > 0:
        return "Win"
    else:
        return "Loss"


game = Game()
game.print_board()
while game.game_over is False:
    if game.players_turn == 1:
        prob, choice = minimax(game.board)
        print("estimated outcome:", outcome(prob))
        print(f"space chosen {choice}")
        game.turn(choice)
    else:
        x = input("Enter the space you would like to go 1-9(left to right, top to bottom):")
        game.turn(x)
