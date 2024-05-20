#/usr/bin/python3

import os
# import console_display
from pynput import keyboard


class Grid():
    def __init__(self, rows, cols):
        self.buttons = {}
        self.rows = rows
        self.cols = cols
        for x in range(rows):
            for y in range(cols):
                self.buttons[(x, y)] = (Button(x, y))

    def __str__(self):
        grid_str = ""
        for x in range(self.rows):
            for y in range(self.cols):
                if self.buttons[(x, y)]._state == True:
                    grid_str += "X "
                elif self.buttons[(x, y)]._state == False:
                    grid_str += "0 "
                else:
                    print("error has occurred, Button.state should be True or False")
            grid_str += '\n'
        return grid_str


class Button():
    def __init__(self, x, y):
        self._state = False  # state is pressed or not
        self.x_pos = None
        self.y_pos = None

    def change_state(self, state):
        if self._state != state:
            self._state = state
        else:
            raise ValueError("This is a redundant button-press")



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def on_press(key):
    try:
        button = Pad.buttons[key_mapper(key)]
        cls()

        if button._state == False:
            button.change_state(True)
            print(Pad)
    except:
        pass

def on_release(key):
    try:
        button = Pad.buttons[key_mapper(key)]
        cls()
        if button._state == True:
            button.change_state(False)
            print(Pad)
    except:
        pass

def key_mapper(key):
    """ This function maps a 4x4 grid from 4 rows x 4 columns on keyboard"""
    if key.char == '1':
        return 0, 0
    elif key.char == '2':
        return 0, 1
    elif key.char == '3':
        return 0, 2
    elif key.char == '4':
        return 0, 3
    ## second row
    elif key.char == 'q':
        return 1, 0
    elif key.char == 'w':
        return 1, 1
    elif key.char == 'e':
        return 1, 2
    elif key.char == 'r':
        return 1, 3
    # Third row
    elif key.char == 'a':
        return 2, 0
    elif key.char == 's':
        return 2, 1
    elif key.char == 'd':
        return 2, 2
    elif key.char == 'f':
        return 2, 3
    ## Fourth row
    elif key.char == 'z':
        return 3, 0
    elif key.char == 'x':
        return 3, 1
    elif key.char == 'c':
        return 3, 2
    elif key.char == 'v':
        return 3, 3


Pad = Grid(4, 4)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

