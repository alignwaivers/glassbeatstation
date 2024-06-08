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
    x = note % 16
    y = int(note / 16)
    y = 7 - y
    press = True if vel == 127 else False
    print (vel)
    KeyPad[x, y](vel)



def basic(*args):
    print (args)

if __name__ == "__main__":

    # instantiate midi ports
    midiout = midi_io.open_virtual_output_port("Launchpad")
    midi_io.create_port_callback("Launchpad", midi_grid_mapping)
    KeyPad = grid.Grid(9, 9)
    KeyPad.buttons[0,0].assign_action(print, "Hello World")
    KeyPad.buttons[1,0].assign_action(test_midi_input, "Hello World")

    KeyPad.buttons[0,0](True)
    print(KeyPad)

    ## launchpad instantiation of functionalities


    while True:
        time.sleep(1)



