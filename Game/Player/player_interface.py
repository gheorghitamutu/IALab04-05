from abc import ABC, abstractmethod


class PlayerInterface(ABC):
    @abstractmethod
    def get_input(self, data):
        pass

    @abstractmethod
    def get_next_move(self, data):
        pass

    @abstractmethod
    def get_move_value(self):
        pass
