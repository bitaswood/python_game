'''
    Name: main.py
    Detail: The main play part of '2048'.
'''


import msvcrt
from modules.game_map import GameMap
from modules.state_controller import StateController


'''
    The main gamer.
'''
class Gamer():

    # ------ Init the checkboard and state controler ------ #
    def __init__(self):

        self.game_map = GameMap()
        self.state_controler = StateController()

    # ------ Check the press ------ #
    def check_press(self, press):

        if press == 'w' or press == 'W':
            return True
        elif press == 'a' or press == 'A':
            return True
        elif press == 's' or press == 'S':
            return True
        elif press == 'd' or press == 'D':
            return True
        elif press == 'r' or press == 'R':
            return True
        elif press == 'q' or press == 'Q':
            return True
        else:
            return None

    # ------ The playing part ------ #
    def play(self):

        # Init operation
        operation = None

        while True:

            # Get the init state and score
            state, score = self.state_controler.state_update(operation)

            # Show the map
            self.game_map.show(state, score)

            # Check whether it is game over
            game_over = self.state_controler.game_over
            if game_over:
                print('GAME OVER!')
                return

            # Get the correct input
            press = None
            while self.check_press(press) is None:
                try:
                    press = msvcrt.getch().decode('ASCII')
                except:
                    continue

            # Restart the game
            if press == 'r' or press == 'R':
                self.game_map = GameMap()
                self.state_controler = StateController()
                operation = None

            # Quit the game
            elif press == 'q' or press == 'Q':
                print('SEE YOU NEXT TIME!')
                return

            # Continue game
            else:
                operation = press


if __name__ == '__main__':

    gamer = Gamer()
    gamer.play()