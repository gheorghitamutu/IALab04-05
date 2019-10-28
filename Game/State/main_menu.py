from Game.State.state import StateInterface
from Game.State.end_state import EndState


class MainMenu(StateInterface):
    def __init__(self, data):
        self.__data = data

    def init(self):
        pass  # nothing to init here

    def handle_input(self):
        choice_index = int(input())

        if choice_index is 1:
            # TODO: description state?
            print("State not implemented!")
        elif choice_index is 2:
            self.__data.get_state_machine().add_state(EndState(self.__data), is_replacing=True)
        else:
            print("Invalid choice!")

    def update(self):
        pass  # nothing to update here

    def draw(self):
        print("\nMINIMAX GAME")
        print("1. Play")
        print("2. Exit")

    def pause(self):
        pass  # nothing to pause here

    def resume(self):
        pass  # nothing to resume here
