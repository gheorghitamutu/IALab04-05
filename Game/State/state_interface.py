from abc import ABC, abstractmethod


class StateInterface(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass
