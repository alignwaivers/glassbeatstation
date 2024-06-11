# /usr/bin/python3

import time
import grid
import midi_io


def grid_to_midi_mapping(x, y):
    return x + y*16

def midi_to_grid_mapping(*args):
    channel, note, vel = args[0]
    x = note % 16
    y = int(note / 16)
    press = True if vel == 127 else False
    KeyPad[x, y].action(press)

if __name__ == "__main__":
    # instantiate midi ports
    LaunchpadOutput = midi_io.MidiOutput("Launchpad", False)
    AltMidi = midi_io.MidiOutput("Alt-output")
    LaunchpadInput = midi_io.MidiInput("Launchpad")
    LaunchpadInput.set_callback(midi_to_grid_mapping)

    KeyPad = grid.Grid(8, 8)

    # # Initial Launchpad Functions loaded
    for y in range(8):
        for x in range(8):
            KeyPad[x, y].append_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(x, y), 127])
            KeyPad[x, y].append_release_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(x, y), 0])



    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        del LaunchpadOutput, LaunchpadInput
        # del AltMidi





