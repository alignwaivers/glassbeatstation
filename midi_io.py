import rtmidi.midiutil

def MidiDevice():
    def __init__():
        pass #

def get_full_port_name(portname, inport=True):
        mididevice = rtmidi.MidiIn() if inport else rtmidi.MidiOut()
        ports = mididevice.get_ports()
        for port in ports:
            try:
                if portname in port:
                    print ("incoming midi port found:", portname, " - connecting")
                    return port
                # else:
                #     print ("unable to find port - ", portname)
            except TypeError:
                print("error in find port ", portname)



def create_port_callback(port_name, function):
    midiin, port_name = rtmidi.midiutil.open_midiinput(get_full_port_name(port_name))
    midiin.set_callback(function)


def send_midi_message(mididevice, note=60, velocity=127, channel=0x90):
    if 0 <= velocity <= 127 and 0 <= note <= 127:
        message = [channel, note, velocity]  # channel 1, middle C, velocity 112
        mididevice.send_message(message)
    else:
        raise ValueError(f"velocity({velocity}) or note({note}) is out of range for midi message. Should be 0-127")



def open_virtual_output_port(name=None):
    # portname = get_full_port_name("")
    MidiOutput = rtmidi.MidiOut()
    available_ports = MidiOutput.get_ports()

    if available_ports:
        for i in range(len(available_ports)):
            if name:
                if name in available_ports[i]:
                    print ("outgoing midi port found", available_ports[i], "- connecting.")
                    MidiOutput.open_port(i)
                    break
    else:
        print (f"port {name} not found")
        MidiOutput.open_virtual_port("My generic virtual output")
    return MidiOutput

