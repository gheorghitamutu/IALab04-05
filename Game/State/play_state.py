from time import sleep
from Game.State.state_interface import StateInterface


class PlayState(StateInterface):
    def __init__(self, data):
        self.__data = data

    def init(self):
        pass  # TODO: maybe init players?

    def handle_input(self):
        pass  # TODO: handle input for each player, taking turns

    def update(self):
        pass

    def draw(self):
        matrix = self.__data.get_field_matrix()
        size = len(matrix)
        index = 0

        for i in matrix:
            for j in i:
                if j is True:
                    print("X ", end="")
                else:
                    print("O ", end="")

                index += 1

                if index == size:
                    print("")
                    index = 0

        for i in range(size * 2):
            print("-", end="")
        print("")

        # TODO: remove the sleep after actions are implemented
        sleep(1)

    def pause(self):
        pass  # get to pause menu

    def resume(self):
        pass  # resume the game
