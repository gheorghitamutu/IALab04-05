from Game.Player.player_interface import PlayerInterface


class HumanPlayer(PlayerInterface):
    def __init__(self):
        self.__matrix_value = -1
        self.current_move = []

    def get_input(self, data):
        while True:
            row = input("Enter # row ")
            col = input("Enter # column ")

            try:  # catch invalid conversions to int from input
                self.current_move = [int(row), int(col)]
            except Exception as e:
                print(e)
                self.current_move = []

            if data.is_valid_move(self.current_move) is True:
                return self.current_move

            self.current_move = []

            print("Invalid input!")

    def get_next_move(self, data):
        return self.current_move

    def get_move_value(self):
        return self.__matrix_value
