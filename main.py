# /usr/bin/python3

import os, time
from pynput import keyboard
import grid
import cpu_keyboard_mapping
import midi_io

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(9):
        print()


def keyaction (key, release):
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


def on_press(key):
    keyaction(key, True)
    print(KeyPad)

def on_release(key):
    keyaction(key, False)
    print(KeyPad)

class MyException(Exception): pass

def test_midi_input(*args):
    channel, note, vel = args[0][0]
    print ("Channel:", channel,"Note:", note,"Velocity:", vel)
    if vel == 127:
        for i in range(127):
            midi_io.send_midi_message(midiout, note, i)
            time.sleep(.001)
        midi_io.send_midi_message(midiout, note, 120)
    else:
        midi_io.send_midi_message(midiout, note, vel)


if __name__ == "__main__":
    computer_key_input = False

    KeyPad = grid.Grid(8, 8)
    # KeyPad[0,0].assign_action(print, "Hello World")
    # KeyPad(0,0)


    # name = midi_io.get_full_port_name("Launchpad")
    midiout = midi_io.open_virtual_output_port("Launchpad")

    # instantiate midi output port and input port by same name (keep output first)
    midi_io.create_port_callback("Launchpad", test_midi_input)

    if computer_key_input:
        os.environ['TERM'] = 'xterm'
        cls()
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            try:
                listener.join()
            except MyException as e:
                print('Exception occurred when {0} was pressed '.format(e.args[0]))
    else:
        while True:
            time.sleep(1)


