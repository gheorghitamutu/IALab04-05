from Game.Player.player_interface import PlayerInterface


class HumanPlayer(PlayerInterface):
    def __init__(self):
        self.__matrix_value = 1
        self.current_move = []

    def get_input(self, data):
        while True:
            row = input("Enter # row\n")
            col = input("Enter # column\n")

            self.current_move = [int(row), int(col)]

            if len(self.get_next_move(data)) == 2:
                return self.current_move

            self.current_move = []

            print("Invalid input!")

    def get_next_move(self, data):
        if data.is_cell_empty(self.current_move):
            return self.current_move

        return []

    def get_move_value(self):
        return self.__matrix_value
