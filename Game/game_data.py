from Game.State.state_machine import StateMachine


class GameData:
    def __init__(self):
        self.__state_machine = StateMachine()

    def get_state_machine(self):
        return self.__state_machine
