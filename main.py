# /usr/bin/python3

import time

import controller
import view
import grid
import midi_io


def grid_to_midi_mapping(x, y):
    # print (x + y*16)
    return x + y*16

if __name__ == "__main__":
    # instantiate midi ports
    LaunchpadOutput = midi_io.MidiOutput("Launchpad", False)
    AltMidi = midi_io.MidiOutput("Alt-output")
    LaunchpadInput = midi_io.MidiInput("Launchpad")

    GridModel = grid.Grid(8, 8, 3)
    GridView = view.GridView(GridModel, LaunchpadOutput)
    GridController = controller.GridController(GridModel, GridView)
    LaunchpadInput.set_callback(GridController.midi_to_grid_mapping)
    # LaunchpadInput.set_callback(print)
    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 115])
        # GridModel[button].set_action(print,grid_to_midi_mapping(*button))
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 0])


    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 100], mode=1)
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 1], mode=1)

    try:
        while True:
            time.sleep(1)


    except KeyboardInterrupt:
        print("exiting")
        GridView.release_leds()



