from Game.State.state_interface import StateInterface


class PlayState(StateInterface):
    def __init__(self, data):
        self.__data = data
        self.__next_move = []
        self.__player_move_value = -1

    def init(self):
        pass  # nothing here

    def handle_input(self):
        player = self.__data.get_current_player()
        self.__next_move = player.get_input(self.__data)
        self.__player_move_value = player.get_move_value()

    def update(self):
        if len(self.__next_move) == 2:
            self.__data.make_move(self.__next_move, self.__player_move_value)

        self.__data.move_to_next_player()

        # TODO: change to end state when win/lose/tie

    def draw(self):
        matrix = self.__data.get_field_matrix()
        size = len(matrix)
        index = 0

        for i in matrix:
            for j in i:
                if j is 1:
                    print("X ", end="")
                elif j is 0:
                    print("O ", end="")
                else:
                    print("_ ", end="")

                index += 1

                if index == size:
                    print("")
                    index = 0

        print("")
        for i in range(size * 2 - 1):
            print("-", end="")
        print("")

    def pause(self):
        pass  # TODO: get to pause menu

    def resume(self):
        pass  # TODO: resume the game
