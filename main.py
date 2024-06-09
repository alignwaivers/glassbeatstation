# /usr/bin/python3

import os, time
import grid
import midi_io


def test_midi_input(*args):
    if vel == 127:
        for i in range(127):
            midi_io.send_midi_message(midiout, note, i)
            time.sleep(.001)
        midi_io.send_midi_message(midiout, note, 120)
    else:
        midi_io.send_midi_message(midiout, note, vel)

def grid_to_midi_mapping(x, y):
    return x + y*16
def midi_to_grid_mapping(*args):
    channel, note, vel = args[0][0]
    x = note % 16
    y = int(note / 16)
    press = True if vel == 127 else False
    print (note)
    KeyPad[x, y](press)

def basic(*args):
    print (args)

if __name__ == "__main__":

    # instantiate midi ports
    midiout = midi_io.open_virtual_output_port("Launchpad")
    midi_io.create_port_callback("Launchpad", midi_to_grid_mapping)
    KeyPad = grid.Grid(8, 8)
    # KeyPad.buttons[0, 0].assign_action(print, "Hello World")
    KeyPad.buttons[0, 0](True)
    KeyPad.buttons[0, 0](False)

    # Initial Launchpad Functions loaded
    for y in range(8):
        for x in range(8):
            KeyPad[x, y].assign_action(print, grid_to_midi_mapping(x, y))
            # KeyPad[x, y].assign_action(print, KeyPad, False)

    while True:
        time.sleep(1)



