# /usr/bin/python3

import time

import grid_controller
import grid_view
import grid_model
import midi_io
from pythonosc import udp_client, dispatcher, osc_server
import osc_interface


def grid_to_midi_mapping(x, y):
    return x + y*16

if __name__ == "__main__":
    # instantiate midi ports
    LaunchpadOutput = midi_io.MidiOutput("Launchpad", False)
    AltMidi = midi_io.MidiOutput("Alt-output")
    LaunchpadInput = midi_io.MidiInput("Launchpad")

    GridModel = grid_model.Grid(8, 8, 3)
    GridView = grid_view.GridView(GridModel, LaunchpadOutput)
    GridController = grid_controller.GridController(GridModel, GridView)
    LaunchpadInput.set_callback(GridController.midi_to_grid_mapping)
    server = osc_server.ThreadingOSCUDPServer(("localhost", 9998), dispatcher)

    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 115])
        # GridModel[button].set_action(print,grid_to_midi_mapping(*button))
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 0])


    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 100], mode=1)
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 1], mode=1)

    # start osc server
    try:
        import osc_server


    except KeyboardInterrupt:
        print("exiting")
        GridView.release_leds()



