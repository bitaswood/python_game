'''
    Name: state_controller.py
    Detail: Update the checkboard state and score by the player input.
'''


import random
import numpy as np


'''
    Control the state and the score.
'''
class StateController():

    # ------ Init the state ------ #
    def __init__(self):
        
        # Init the state and the score
        self.state = np.zeros((4, 4), dtype=int)
        self.score = 0

        # Init the zero list which is used to random generation
        self.zero_list = [[0,0],[0,1],[0,2],[0,3],
                          [1,0],[1,1],[1,2],[1,3],
                          [2,0],[2,1],[2,2],[2,3],
                          [3,0],[3,1],[3,2],[3,3]]

        # Init the game over state
        self.game_over = False

        # Randomly generate the first part
        self.random_generate()

    # ------ Generate a non-zero number randomly ------ #
    def random_generate(self):

        # Random number you can choose
        random_list = [2, 4]

        # Randomly generate a position and a 
        length = len(self.zero_list)
        if length == 0:
            return
        random_position = random.randint(0, length-1)
        position_on_check = self.zero_list[random_position]
        random_number = random_list[random.randint(0, 1)]

        # Delete the position from the zero list
        self.zero_list.pop(random_position)

        # Update the state
        self.state[position_on_check[0], position_on_check[1]] = random_number

    # ------ Judge whether it is game over ------ #
    def game_over_judge(self):

        # Pad to ease the judgement
        dilated_state = np.pad(self.state, 1, mode='constant')

        # If you cannot find a same number in a neighbour place, then game is over
        for i in range(1,5):
            for j in range(1,5):
                if dilated_state[i,j] == dilated_state[i-1,j]:
                    return False
                elif dilated_state[i,j] == dilated_state[i+1,j]:
                    return False
                elif dilated_state[i,j] == dilated_state[i,j-1]:
                    return False
                elif dilated_state[i,j] == dilated_state[i,j+1]:
                    return False
        return True

    # ------ Get the neighbour ------ #
    def get_neighbour(self, i, j, operation):

        if operation == 'w' or operation == 'W':
            return i-1, j
        elif operation == 'a' or operation == 'A':
            return i, j-1
        elif operation == 's' or operation == 'S':
            return i+1, j
        elif operation == 'd' or operation == 'D':
            return i, j+1

    # ------ Get the current number ------ #
    def get_current(self, i, j, operation):

        if operation == 'w' or operation == 'W':
            return i, j
        elif operation == 'a' or operation == 'A':
            return i, j
        elif operation == 's' or operation == 'S':
            return 3-i, j
        elif operation == 'd' or operation == 'D':
            return i, 3-j

    # ------ Change the state by operation ------ #
    def state_change(self, operation):

        # Memorize the old state 
        old_state = self.state.copy()

        # Different operation lead to different change
        for i in range(4):
            for j in range(4):
                x1, y1 = self.get_current(i, j, operation)
                x2, y2 = self.get_neighbour(x1, y1, operation)
                # If the neighbour is out of boundary, break
                while(x2 != -1 and x2 != 4 and y2 != -1 and y2 != 4):
                    # Current element is not zero
                    if self.state[x1,y1] != 0:
                        # If the element above is equal to the current, add and move
                        if self.state[x2,y2] == self.state[x1,y1]:
                            # Update the state
                            self.score += self.state[x1,y1]
                            self.state[x2,y2] += self.state[x1,y1]
                            self.state[x1,y1] = 0
                            # Update the zero list
                            self.zero_list.append([x1,y1])
                        # If the element above is zero, add and move
                        elif self.state[x2,y2] == 0:
                            # Update the state
                            self.state[x2,y2] += self.state[x1,y1]
                            self.state[x1,y1] = 0
                            # Update the zero list
                            self.zero_list.append([x1,y1])
                            self.zero_list.remove([x2,y2])
                    # Update the position
                    x1, y1 = x2, y2
                    x2, y2 = self.get_neighbour(x1, y1, operation)

        # Choose wether to generate a number, not equal then generate
        if not np.array_equal(old_state, self.state):
            self.random_generate()

    # ------ The main part of state update ------ #
    def state_update(self, operation=None):
        
        # No operation, return directly
        if operation == None:
            return self.state, self.score

        # Change the state
        self.state_change(operation)

        # Check whether it is game over
        self.game_over = self.game_over_judge()

        # Output the state and the score
        return self.state, self.score