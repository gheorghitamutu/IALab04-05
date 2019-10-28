from Game.State.state_machine import StateMachine


class GameData:
    def __init__(self):
        self.__state_machine = StateMachine()
        self.__matrix_size = 3  # can always make this as an options for a bigger matrix instead hard coding it
        self.__matrix_generator = lambda n: [[0 for i in range(n)] for j in range(n)]  # of squared matrix
        self.__field_matrix = self.__matrix_generator(self.__matrix_size)
        self.__player_list = []  # this would allow X numbers of players and it will be used in PlayState class

    def get_state_machine(self):
        return self.__state_machine

    def get_field_matrix(self):
        return self.__field_matrix
