from Game.Player.player_interface import PlayerInterface


class AIPlayer(PlayerInterface):
    def __init__(self):
        self.__matrix_value = 0

    def get_input(self, data):
        return self.get_next_move(data)

    def get_next_move(self, data):
        return data.get_best_move_indexes(self.__matrix_value)

    def get_move_value(self):
        return self.__matrix_value
