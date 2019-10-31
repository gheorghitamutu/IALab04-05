from math import inf
from Game.State.state_machine import StateMachine
from Game.Player.AI_player import AIPlayer
from Game.Player.human_player import HumanPlayer


class GameData:
    def __init__(self):
        self.__state_machine = StateMachine()
        self.__matrix_size = 3
        self.__empty_cell = 0
        self.__matrix_generator = lambda n: [[self.__empty_cell for i in range(n)] for j in range(n)]
        self.__board = self.__matrix_generator(self.__matrix_size)
        self.__player_list = [HumanPlayer(), AIPlayer()]
        self.__evaluate_good = 1
        self.__evaluate_bad = -1
        self.__evaluate_neutral = 0
        self.__current_player_index = 0
        self.__game_title = "TIC TAC TOE"
        self.__human_value = -1
        self.__AI_value = 1

    def get_state_machine(self):
        return self.__state_machine

    def get_board(self):
        return self.__board

    def get_current_player(self):
        return self.__player_list[self.__current_player_index]

    def move_to_next_player(self):
        if self.__current_player_index < len(self.__player_list) - 1:
            self.__current_player_index += 1
        else:
            self.__current_player_index = 0

    def get_game_title(self):
        return self.__game_title

    def generate_clean_matrix(self):
        self.__board = self.__matrix_generator(self.__matrix_size)

    def make_move(self, move, value):
        self.__board[move[0]][move[1]] = value

    def win(self, player_value):

        win_states = [
            [self.__board[0][0], self.__board[0][1], self.__board[0][2]],
            [self.__board[1][0], self.__board[1][1], self.__board[1][2]],
            [self.__board[2][0], self.__board[2][1], self.__board[2][2]],
            [self.__board[0][0], self.__board[1][0], self.__board[2][0]],
            [self.__board[0][1], self.__board[1][1], self.__board[2][1]],
            [self.__board[0][2], self.__board[1][2], self.__board[2][2]],
            [self.__board[0][0], self.__board[1][1], self.__board[2][2]],
            [self.__board[2][0], self.__board[1][1], self.__board[0][2]],
        ]

        return [player_value, player_value, player_value] in win_states

    def evaluate_state(self):
        if self.win(self.__AI_value):
            score = self.__evaluate_good
        elif self.win(self.__human_value):
            score = self.__evaluate_bad
        else:
            score = self.__evaluate_neutral

        return score

    def is_game_over(self):
        return self.win(self.__AI_value) or self.win(self.__human_value)

    def get_empty_cells(self):
        cells = []

        for x, row in enumerate(self.__board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def is_valid_move(self, move):
        if move in self.get_empty_cells():
            return True
        else:
            return False

    def minimax(self, depth, player_cell_value, alpha, beta):
        if player_cell_value == self.__AI_value:
            best_move_score = [-inf, -inf, -inf]
        else:
            best_move_score = [-inf, -inf, +inf]

        if depth is 0 or self.is_game_over():  # first level or final state (win/lose/tie)
            this_move_score = self.evaluate_state()
            return [-inf, -inf, this_move_score]

        for cell in self.get_empty_cells():
            self.__board[cell[0]][cell[1]] = player_cell_value

            this_move_score = self.minimax(depth - 1, -player_cell_value, alpha, beta)

            self.__board[cell[0]][cell[1]] = self.__empty_cell
            this_move_score[0], this_move_score[1] = cell[0], cell[1]

            if player_cell_value == self.__AI_value:  # maximizer
                if this_move_score[2] > best_move_score[2]:
                    best_move_score = this_move_score

                    # alpha-beta pruning maximizer
                    if best_move_score[2] >= beta:
                        return best_move_score

                    if best_move_score[2] > alpha:
                        alpha = best_move_score[2]

            else:  # minimizer
                if this_move_score[2] < best_move_score[2]:
                    best_move_score = this_move_score

                    # alpha-beta pruning minimizer
                    if best_move_score[2] <= alpha:
                        return best_move_score

                    if best_move_score[2] < beta:
                        beta = best_move_score[2]

        return best_move_score

    def get_best_move(self):
        depth = len(self.get_empty_cells())

        if depth == 0 or self.is_game_over():
            return None  # game is over already

        if depth == 9:  # handle the case when the AI is first
            move = [0, 0]
        else:
            row, col, score = self.minimax(depth, self.__AI_value, -inf, inf)
            move = [row, col]

        return move
