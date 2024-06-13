# /usr/bin/python3

import time

import controller
import view
import grid
import midi_io


def grid_to_midi_mapping(x, y):
    return x + y*16

if __name__ == "__main__":
    # instantiate midi ports
    LaunchpadOutput = midi_io.MidiOutput("Launchpad", False)
    AltMidi = midi_io.MidiOutput("Alt-output")
    LaunchpadInput = midi_io.MidiInput("Launchpad")

    GridModel = grid.Grid(8, 8)
    GridView = view.GridView(GridModel)
    GridController = controller.GridController(GridModel, GridView)
    LaunchpadInput.set_callback(GridController.midi_to_grid_mapping)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")



