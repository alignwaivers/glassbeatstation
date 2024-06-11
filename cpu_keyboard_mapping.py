import os, sys
from pynput import keyboard
os.environ['TERM'] = 'xterm'

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(9):
        print()


def on_release(key):
    keyaction(key, False)


def keyaction(key, release):
    try:
        keychar = key.char
        button = KeyPad.buttons[cpu_keyboard_mapping.key_mapper(keychar)]
        try:
            if button._state != release:
                button.change_state(True)
            else:
                print(f"Redundant key action, already registered in {button._state}")
        except (KeyError):
            print("Unregistered keypress", key)
    except  (AttributeError):
        pass


def key_mapper(key):
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
    else:
        return None


cls()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except MyException as e:
        print('Exception occurred when {0} was pressed '.format(e.args[0]))


def on_press(key):
    keyaction(key, True)


