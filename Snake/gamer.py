'''
    Name: main.py
    Detail: The main play part of 'Snake'.
'''


import time
import msvcrt
import threading
from modules.game_map import GameMap
from modules.constant_define import *
from modules.state_controller import StateController


'''
    The main gamer.
'''
class Gamer():

    # ------ Init the checkboard and state controler ------ #
    def __init__(self):

        self.game_map = GameMap()
        self.state_controler = StateController()
        self.operation = None

    # ------ Check the press ------ #
    def check_press(self, press):

        if press == 'w' or press == 'W':
            return UP
        elif press == 'a' or press == 'A':
            return LEFT
        elif press == 's' or press == 'S':
            return DOWN
        elif press == 'd' or press == 'D':
            return RIGHT
        elif press == 'r' or press == 'R':
            return True
        elif press == 'q' or press == 'Q':
            return True
        else:
            return None

    # ------ Get the keyboard input ------ #
    def input_get(self):

        while True:

            # Get the correct input
            press = None
            while self.check_press(press) is None:
                try:
                    press = msvcrt.getch().decode('ASCII')
                except:
                    continue

            # Update the operation
            self.operation = press

    # ------ The playing part ------ #
    def play(self):

        # Create multi-threading
        t = threading.Thread(target=self.input_get)
        t.setDaemon(True)
        t.start()

        while True:

            # Get the init state and score
            state, score = self.state_controler.state_update(self.operation)

            # Show the map
            self.game_map.show(state, score)

            # Check whether it is game over
            game_over = self.state_controler.game_over
            if game_over:
                print('GAME OVER!')
                exit(0)

            # Restart the game
            if self.operation == 'r' or self.operation == 'R':
                self.game_map = GameMap()
                self.state_controler = StateController()
                self.operation = None

            # Quit the game
            elif self.operation == 'q' or self.operation == 'Q':
                print('SEE YOU NEXT TIME!')
                exit(0)

            # Wait for some seconds
            time.sleep(0.03)


if __name__ == '__main__':

    gamer = Gamer()
    gamer.play()