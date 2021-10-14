'''
    Name: map.py
    Detail: Define the main UI part for the 2048 game, include map, score.
    Example:
    ---------------------------------------------------
    - YOUR SCORE: XXXX                                -
    -                                                 -
    -             * * * * * * * * * * *               -
    -             *    *    *    *    *               -
    -             * * * * * * * * * * *               -
    -             *    *    *    *    *               -
    -             * * * * * * * * * * *               -
    -             *    *    *    *    *               -
    -             * * * * * * * * * * *               -
    -             *    *    *    *    *               -
    -             * * * * * * * * * * *               -
    -                                                 -
    - Press W/A/S/D to play, R to restart, Q to quit. -
    ---------------------------------------------------
'''


import os
import numpy as np


'''
    The map of the 2048 game.
'''
class GameMap():

    # ------ Init the whole map ------ #
    def __init__(self):

        # The score for the player
        self.score = 0

        # The state of the checkboard
        self.state = np.zeros((4, 4), dtype=int)

    # ------ Update the state of the checkboard and the score of the checkboard ------ #
    def update(self, state, score):
        if type(state) == np.ndarray:
            self.state = state
            self.score = score

    # ------ Draw a map using state and score ------ #
    def draw(self):

        score = self.score
        state = self.state

        print(
              '---------------------------------------------------\n' \
            + '- YOUR SCORE: {:>4d}                                -\n'.format(score) \
            + '-                                                 -\n' \
            + '-             * * * * * * * * * * *               -\n' \
            + '-             *{:^4d}*{:^4d}*{:^4d}*{:^4d}*               -\n'.format(state[0,0],state[0,1],state[0,2],state[0,3]) \
            + '-             * * * * * * * * * * *               -\n' \
            + '-             *{:^4d}*{:^4d}*{:^4d}*{:^4d}*               -\n'.format(state[1,0],state[1,1],state[1,2],state[1,3]) \
            + '-             * * * * * * * * * * *               -\n' \
            + '-             *{:^4d}*{:^4d}*{:^4d}*{:^4d}*               -\n'.format(state[2,0],state[2,1],state[2,2],state[2,3]) \
            + '-             * * * * * * * * * * *               -\n' \
            + '-             *{:^4d}*{:^4d}*{:^4d}*{:^4d}*               -\n'.format(state[3,0],state[3,1],state[3,2],state[3,3]) \
            + '-             * * * * * * * * * * *               -\n' \
            + '-                                                 -\n' \
            + '- Press W/A/S/D to play, R to restart, Q to quit. -\n' \
            + '---------------------------------------------------'
        )


    # ------ Show the whole checkboard ------ #
    def show(self, state=None, score=None):
        
        # Update the parameters
        self.update(state, score)

        # Clean the screen
        os.system('cls')

        # Draw another map
        self.draw()