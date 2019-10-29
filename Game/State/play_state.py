from Game.State.state_interface import StateInterface
from Game.State.end_state import EndState


class PlayState(StateInterface):
    def __init__(self, data):
        self.__data = data
        self.__next_move = []
        self.__player_move_value = -1
        self.__tie = 0
        self.__AI_won = 0
        self.__human_won = 0

    def init(self):
        pass  # nothing here

    def handle_input(self):
        player = self.__data.get_current_player()
        self.__next_move = player.get_input(self.__data)
        self.__player_move_value = player.get_move_value()

    def update(self):
        if self.__tie or self.__AI_won or self.__human_won:
            self.__data.get_state_machine().add_state(EndState(self.__data), is_replacing=True)

        if len(self.__next_move) == 2:
            self.__data.make_move(self.__next_move, self.__player_move_value)

        end_game = self.__data.evaluate_matrix()
        if end_game is not 0:
            if end_game is 1:
                self.__human_won = 1
            elif end_game is -1:
                self.__AI_won = 1

        if self.__data.are_empty_cells() is not True:
            self.__tie = 1

        self.__data.move_to_next_player()

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

        if self.__human_won:
            print("Human won!")

        if self.__AI_won:
            print("AI won!")

        if self.__tie:
            print("Tie between Human and AI")

    def pause(self):
        pass  # TODO: get to pause menu

    def resume(self):
        pass  # TODO: resume the game
