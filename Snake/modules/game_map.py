'''
    Name: game_map.py
    Detail: Define the main UI part for the 'Snake' game, include map, score.
    Example:
    -------------------------------------------------------------------------------------------
    - YOUR SCORE: XXXX                                                                        -
    -                                                                                         -
    - # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                           @                         # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                              000000X                                                # -
    - #                              0                                                      # -
    - #                              0                                                      # -
    - #                              0                                                      # -
    - #                    00000000000                                                      # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - #                                                                                     # -
    - # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # -
    -                                                                                         -
    - PRESS W/A/S/D TO PLAY, R TO RESTART, Q TO QUIT.                                         -
    -------------------------------------------------------------------------------------------
'''


import os
import numpy as np
from modules.constant_define import *


'''
    The map of the 'Snake' game.
'''
class GameMap():

    # ------ Init the whole map ------ #
    def __init__(self):

        # The score for the player
        self.score = 0

        # The state for the game
        self.state = np.zeros((20, 85), dtype=int)

    # ------ Update the state of the game and the score of the game ------ #
    def update(self, state, score):
        if type(state) == np.ndarray:
            self.state = state
            self.score = score

    # ------ Draw a map using state and score ------ #
    def draw(self):

        score = self.score
        state = self.state

        print(
            '-------------------------------------------------------------------------------------------\n' \
          + '- YOUR SCORE: {:>4d}                                                                        -\n'.format(score) \
          + '-                                                                                         -\n' \
          + '- # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # -'
        )

        for idx in range(20):
            state_for_line = ''
            for num in range(85):
                state_for_line += draw_pic[state[idx, num]]
            print('- #' + state_for_line + '# -')

        print(
            '- # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # -\n' \
          + '-                                                                                         -\n' \
          + '- PRESS W/A/S/D TO PLAY, R TO RESTART, Q TO QUIT.                                         -\n' \
          + '-------------------------------------------------------------------------------------------'
        )

    # ------ Show the whole checkboard ------ #
    def show(self, state=None, score=None):
        
        # Update the parameters
        self.update(state, score)

        # Clean the screen
        os.system('cls')

        # Draw another map
        self.draw()