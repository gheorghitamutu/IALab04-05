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
        self.__symbols = {-1: 'X', 1: 'O', 0: ' '}
        self.__delimiter = '---------------'

    def init(self):
        pass  # nothing here

    def handle_input(self):
        if not self.__data.is_game_over():
            player = self.__data.get_current_player()
            self.__next_move = player.get_input(self.__data)
            self.__player_move_value = player.get_move_value()

    def update(self):
        if self.__tie or self.__AI_won or self.__human_won:
            self.__data.get_state_machine().add_state(EndState(self.__data), is_replacing=True)

        if self.__data.is_valid_move(self.__next_move):
            self.__data.make_move(self.__next_move, self.__player_move_value)
            self.__data.move_to_next_player()

        if self.__data.is_game_over():
            self.__human_won = self.__data.win(-1)  # hardcoded human value
            self.__AI_won = self.__data.win(1)      # hardcoded AI value
        elif len(self.__data.get_empty_cells()) is 0:
            self.__tie = True

    def draw(self):
        if self.__player_move_value is 1:  # hardcoded AI value
            print("AI turn")
        else:
            print("Human turn")

        print('{}'.format(self.__delimiter))
        for row in self.__data.get_board():
            for cell in row:
                print('|{}|'.format(self.__symbols[cell]), end="")
            print("")
        print('\n{}'.format(self.__delimiter))

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
