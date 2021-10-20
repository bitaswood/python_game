'''
    Name: constant_define.py
    Detail: Define some constants in the game.
'''


# ------ Constant for map state ------ #
NOTHING = 0
HEAD = 1
BODY = 2
TAIL = 3
FRUIT = 4

draw_pic = {
    NOTHING : ' ',
    HEAD : 'X',
    BODY : '0',
    TAIL : '0',
    FRUIT : '@'
}

# ------ Constant for direction ------ #
RIGHT = 'd'
LEFT = 'a'
UP = 'w'
DOWN = 's'