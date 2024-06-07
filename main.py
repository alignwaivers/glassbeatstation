# /usr/bin/python3

import os, time

import grid
import midi_io


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

def midi_grid_mapping(*args):
    channel, note, vel = args[0][0]


if __name__ == "__main__":

    # instantiate midi ports
    midiout = midi_io.open_virtual_output_port("Launchpad")
    midi_io.create_port_callback("Launchpad", test_midi_input)

    KeyPad = grid.Grid(8, 8)
    # KeyPad[0,0].assign_action(print, "Hello World")
    # KeyPad[0,0].assign_action(midi_io.send_midi_message()
    KeyPad[0,0](True)


    while True:
        time.sleep(1)



