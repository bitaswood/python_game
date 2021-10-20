'''
    Name: state_controller.py
    Detail: Update the game state and score by the player input.
'''


import random
import numpy as np
from modules.constant_define import *


'''
    Control the state and the score.
'''
class StateController():

    # ------ Init the state ------ #
    def __init__(self):

        # Init the state and the score
        self.snake = []
        self.state = np.zeros((20, 85), dtype=int)
        for idx in range(3):
            self.state[10, idx+5] = BODY
            self.snake.append([10, idx+5])
        self.state[10, 8] = HEAD
        self.snake.append([10, 8])

        self.score = 0

        # Init the nothing list
        self.nothing_list = []
        for i in range(20):
            for j in range(85):
                if self.state[i, j] == NOTHING:
                    self.nothing_list.append([i, j])

        # Init the game over state
        self.game_over = False

        # Init the direction
        self.direction = RIGHT

        # Generate a fruit
        self.fruit_generate()

    # ------ Generate a fruit ------ #
    def fruit_generate(self):

        # Genarate a fruit in a random position
        length = len(self.nothing_list)
        if length == 0:
            return
        random_position = random.randint(0, length-1)
        position_on_map = self.nothing_list[random_position]

        # Update the map state
        self.state[position_on_map[0], position_on_map[1]] = FRUIT
        self.nothing_list.pop(random_position)

    # ------ Judge the direction ------ #
    def direction_judge(self):

        if self.direction == RIGHT:
            return 0, 1
        elif self.direction == LEFT:
            return 0, -1
        elif self.direction == UP:
            return -1, 0
        elif self.direction == DOWN:
            return 1, 0
        else:
            return None, None

    # ------ Check whether the direction is right ------ #
    def direction_check(self, old_direction):

        i, j = self.direction_judge()
        head = self.snake[-1]
        head_before = self.snake[-2]
        if (head[0]+i) == head_before[0] and (head[1]+j) == head_before[1]:
            self.direction = old_direction
            i, j = self.direction_judge()
        return i, j

    # ------ Define the 'eat' action ------ #
    def snake_eat(self, i, j):

        # Fruit becomes new head
        head = self.snake[-1]
        self.state[head[0]+i, head[1]+j] = HEAD
        self.state[head[0], head[1]] = BODY
        # Put the fruit position into the snake
        self.snake.append([head[0]+i, head[1]+j])
        # Update the score
        self.score += len(self.snake)
        # Generate a new fruit
        self.fruit_generate()

    # ------ Define the 'move' action ------ #
    def snake_move(self, i, j):

        # Head change and tail delete
        head = self.snake[-1]
        tail = self.snake[0]
        self.state[head[0]+i, head[1]+j] = HEAD
        self.state[head[0], head[1]] = BODY
        self.state[tail[0], tail[1]] = NOTHING
        # Add new head and remove old tail
        self.snake.append([head[0]+i, head[1]+j])
        self.snake.pop(0)

    # ------ Judge whether game over ------ #
    def judge_game_over(self, i, j):

        head = self.snake[-1]

        # Judge whether it is wall
        if (head[0]+i) < 0 or (head[0]+i) > 19:
            self.game_over = True
            return
        elif (head[1]+j) < 0 or (head[1]+j) > 84:
            self.game_over = True
            return

        # Judge whether it is body
        if self.state[head[0]+i, head[1]+j] == BODY:
            self.game_over = True
            return
        elif self.state[head[0]+i, head[1]+j] == FRUIT:
            return FRUIT
        elif self.state[head[0]+i, head[1]+j] == NOTHING:
            return NOTHING

    # ------ The main part of state update ------ #
    def state_update(self, operation=None):
        
        # Record the old direction
        old_direction = self.direction

        # Update direction
        if operation == RIGHT or operation == LEFT or operation == UP or operation == DOWN:
            self.direction = operation

        # Get the direction
        i, j = self.direction_check(old_direction)

        # Judge whether it is game over
        next_block = self.judge_game_over(i, j)
        if self.game_over:
            return self.state, self.score

        # Choose to eat or move
        if next_block == FRUIT:
            self.snake_eat(i, j)
        elif next_block == NOTHING:
            self.snake_move(i, j)

        # Output the state and the score
        return self.state, self.score
