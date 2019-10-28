from abc import ABC, abstractmethod


class PlayerInterface(ABC):
    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def next_move(self):
        pass
