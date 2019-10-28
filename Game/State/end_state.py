import time
from Game.State.state import StateInterface


class EndState(StateInterface):
    def __init__(self, data):
        self.__data = data
        self.__message_shown = False

    def init(self):
        pass  # nothing to init here

    def handle_input(self):
        pass  # nothing to handle here

    def update(self):
        time.sleep(3)

    def draw(self):
        if not self.__message_shown:
            print("Thank you for playing!")
            self.__message_shown = True
        else:
            exit(0)  # end game; close process

    def pause(self):
        pass  # nothing to pause here

    def resume(self):
        pass  # nothing to resume here
