import rtmidi2

class MidiOutput:
    def __init__(self, port_name, virtual=True, unicode=None):

        self.midi_out = rtmidi2.MidiOut(unicode)
        ports = self.midi_out.ports
        found = False
        if virtual:
            print(f"Opening New Virtual MIDI output port: {port_name}")
            self.midi_out.open_virtual_port(port_name)
        else:
            found = False
            for i in range(len(ports)):
                if port_name in ports[i]:
                    print(f"Opening MIDI output port: {ports[i]}")
                    self.midi_out.open_port (i)
                    found = True
            if found == False:
                print (port_name, "port not found")


    def send_messages(self, note=60, velocity=127, channel=0x90):
        if 0 <= velocity <= 127 and 0 <= note <= 127:
            message = [channel, note, velocity]  # channel 1, middle C, velocity 112
            self.midi_out.send_noteon(*message)
        else:
            raise ValueError(f"velocity({velocity}) or note({note}) is out of range for midi message. Should be 0-127")



class MidiInput():
    def __init__(self, port_name:str):
        self.midi_in = rtmidi2.MidiIn()
        ports = self.midi_in.ports
        if not ports:
            print("No MIDI input ports available.")
        else:
            for i in range(len(ports)):
                if port_name in ports[i]:
                    print(f"Opening MIDI input port: {ports[i]}")
                    self.midi_in.open_port(i)

    # Set the callback function for incoming MIDI messages
    def set_callback(self, callback_func):
        self.midi_in.callback = callback_func

    def __del__(self):
        self.midi_in.close_port()
