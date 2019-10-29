from Game.State.state_machine import StateMachine
from Game.Player.AI_player import AIPlayer
from Game.Player.human_player import HumanPlayer


class GameData:
    def __init__(self):
        self.__state_machine = StateMachine()
        self.__matrix_size = 3  # can always make this as an options for a bigger matrix instead hard coding it
        self.__empty_cell = self.__matrix_size + 1
        self.__matrix_generator = lambda n: [[self.__empty_cell for i in range(n)] for j in range(n)]
        self.__field_matrix = self.__matrix_generator(self.__matrix_size)
        self.__player_list = [
            HumanPlayer(),
            AIPlayer()
        ]  # this would allow X numbers of players and it will be used in PlayState class
        self.__evaluate_good = 1
        self.__evaluate_bad = -1
        self.__evaluate_neutral = 0
        self.__current_player_index = 0

    def get_state_machine(self):
        return self.__state_machine

    def get_field_matrix(self):
        return self.__field_matrix

    def get_current_player(self):
        return self.__player_list[self.__current_player_index]

    def move_to_next_player(self):
        if self.__current_player_index < len(self.__player_list) - 1:
            self.__current_player_index += 1
        else:
            self.__current_player_index = 0

    def make_move(self, move, value):
        self.__field_matrix[move[0]][move[1]] = value

    def is_cell_empty(self, next_move):
        return self.__field_matrix[next_move[0]][next_move[1]] == self.__empty_cell

    # Returns a value based on who is winning (-1, 0, 1).
    def evaluate_matrix(self):
        # check victory on rows
        for row in self.__field_matrix:
            if sum(row) == self.__matrix_size:
                return self.__evaluate_good  # "X"
            elif sum(row) == 0:
                return self.__evaluate_bad  # "O"

        # check victory on columns
        for col in zip(*self.__field_matrix):
            if sum(col) == self.__matrix_size:
                return self.__evaluate_good  # "X"
            elif sum(col) == 0:
                return self.__evaluate_bad  # "O"

        # check victory on diagonals
        if sum(self.__field_matrix[i][i] for i in range(self.__matrix_size)) == self.__matrix_size:
            return self.__evaluate_good  # "X"
        elif sum(self.__field_matrix[i][i] for i in range(self.__matrix_size)) == 0:
            return self.__evaluate_bad  # "O"

        if sum(self.__field_matrix[self.__matrix_size - i - 1][self.__matrix_size - i - 1]
               for i in range(self.__matrix_size)) == self.__matrix_size:
            return self.__evaluate_good  # "X"
        elif sum(self.__field_matrix[self.__matrix_size - i - 1][self.__matrix_size - i - 1]
                 for i in range(self.__matrix_size)) == 0:
            return self.__evaluate_bad  # "O"

        return self.__evaluate_neutral

    # Returns if there are any uncompleted cells left in the matrix.
    def are_empty_cells(self):
        for row in self.__field_matrix:
            if self.__empty_cell in row:
                return True

        return False

    # Minimax algorithm
    def minimax(self, depth, is_max):
        score = self.evaluate_matrix()

        # Maximizer won
        if score == self.__evaluate_good:
            return score

        # Minimizer won
        if score == self.__evaluate_bad:
            return score

        # Tie
        if not self.are_empty_cells():
            return self.__evaluate_neutral

        best = 100
        if is_max:
            best = -100

        for i in range(self.__matrix_size):
            for j in range(self.__matrix_size):
                if self.__field_matrix[i][j] == self.__empty_cell:

                    # move
                    self.__field_matrix[i][j] = 1 if is_max else 0  # X or O

                    # choose the maximum value
                    best = max(best, self.minimax(depth + 1, not is_max)) if is_max \
                        else min(best, self.minimax(depth + 1, not is_max))

                    # undo the move
                    self.__field_matrix[i][j] = self.__empty_cell

        return best

    # Return best move [row, col] where player matrix value is 0 or 1 (O or X)
    def get_best_move_indexes(self, player_matrix_value):
        best_value = -100
        best_row = -1
        best_col = -1

        for i in range(self.__matrix_size):
            for j in range(self.__matrix_size):
                if self.__field_matrix[i][j] == self.__empty_cell:

                    # move
                    self.__field_matrix[i][j] = player_matrix_value

                    # choose the maximum value for this move
                    current_move_value = self.minimax(0, True)

                    # TODO: remove message when it is not needed anymore
                    print("AI current move value: {}".format(current_move_value))

                    # undo the move
                    self.__field_matrix[i][j] = self.__empty_cell

                    # is this the best move up until now?
                    if current_move_value > best_value:
                        best_row = i
                        best_col = j
                        best_value = current_move_value

        return [best_row, best_col]
