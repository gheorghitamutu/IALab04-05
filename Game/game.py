from Game.game_data import GameData
from Game.State.splash_state import SplashState


class Game:
    def __init__(self):
        self.__data = GameData()
        self.__data.get_state_machine().add_state(SplashState(self.__data), is_replacing=True)
        self.__data.get_state_machine().process_state_changes()

    def run(self):
        while True:
            self.__data.get_state_machine().get_active_state().handle_input()
            self.__data.get_state_machine().get_active_state().update()
            self.__data.get_state_machine().process_state_changes()
            self.__data.get_state_machine().get_active_state().draw()
