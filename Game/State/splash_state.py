import time
from Game.State.state import StateInterface


class SplashState(StateInterface):
    def __init__(self, data):
        self.__data = data
        self.__state_duration = 3
        self.__current_count = 0

    def init(self):
        pass  # nothing to init here

    def handle_input(self):
        pass  # nothing to handle here

    def update(self):
        if self.__current_count == self.__state_duration:
            # TODO: add main menu state
            # self.__data.machine.add_state(MainMenu(data))
            print("Should add main menu? -> Force close the script for now")
        else:
            self.__current_count += 1

    def draw(self):
        print("\rMinimax Game {}".format(self.__state_duration - self.__current_count))

        time.sleep(1)

    def pause(self):
        pass  # nothing to pause here

    def resume(self):
        pass  # nothing to resume here
