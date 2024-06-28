# /usr/bin/python3

import time

import grid_controller
import grid_view
import grid_model
import looper
import midi_io
import osc_server
import osc_sender
# from pythonosc import udp_client, dispatcher, osc_server
# import osc_interface

def grid_to_midi_mapping(x, y):
    return x + y*16

if __name__ == "__main__":
    # instantiate Launchpad midi ports
    LaunchpadOutput = midi_io.MidiOutput("Launchpad", False)
    # AltMidi = midi_io.MidiOutput("Alt-output")
    LaunchpadInput = midi_io.MidiInput("Launchpad")

    # Instantiate grid model, view, and controller
    GridModel = grid_model.Grid(8, 8, 3)
    GridView = grid_view.GridView(GridModel, LaunchpadOutput)
    GridController = grid_controller.GridController(GridModel, GridView)

    # Set the callback for the midi input
    LaunchpadInput.set_callback(GridController.midi_to_grid_mapping)

    # start osc server
    osc_server = osc_server.OSC_Receiver()

    # instantiate sooperlooper
    LooperOSC_output = osc_sender.OSC_Sender()
    SooperLooper = looper.Looper(8, LooperOSC_output, "9981")
    osc_server.add_handler("/sloop", SooperLooper.handle_input)

    # set launchpad Led actions for buttons mode 0
    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 7])
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 0])

    # set launchpad Led actions for buttons mode 1
    for button in GridModel.grid.keys():
        GridModel[button].set_action(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 100], mode=1)
        GridModel[button].set_release(LaunchpadOutput.send_messages, [grid_to_midi_mapping(*button), 1], mode=1)

    # set launchpad actions for mode 0 (SooperLooper)
    row_actions = ["record", "overdub", "oneshot", "trigger", "pause", "reverse", "undo", "redo"]
    for y in range(8):
        for x in range(8):
            GridModel[x, y].set_action(SooperLooper[y].loop_action, row_actions[x])

    while True:
        try:
            time.sleep(.005)
            osc_server.server_thread.join()



        except KeyboardInterrupt:
            print("exiting")
            osc_server.shutdown()
            GridView.release_leds()




