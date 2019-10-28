import time
from Game import game_data


class Game:
    data = game_data.GameData

    @staticmethod
    def run():

        while True:
            print('GameData.run()')

            '''
                TODO: from current state on queue handle user input
                TODO: from current state on queue update
                TODO: from current state on queue process state changes
                TODO: from current state on queue draw (console stuff)
            '''

            time.sleep(1)  # TODO: remove this after you implement the above TODOs
