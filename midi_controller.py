import sys
import rtmidi.midiutil
import time

def MidiDevice():
    pass # placeholder

def get_full_port_name(name, inport=True):
        mididevice = rtmidi.MidiIn() if inport else rtmidi.MidiOut()
        ports = mididevice.get_ports()
        for port in ports:
            try:
                if name in port:
                    return port
            except:
                print("failure to return port")
            # finally:
            #     mididevice.delete()



def send_midi_message(mididevice, note=60, velocity=127, channel=0x90):
    if 0 <= velocity <= 127:
        message = [channel, note, velocity]  # channel 1, middle C, velocity 112
        mididevice.send_message(message)
    else:
        raise ValueError(velocity, "velocity is out of range for midi message. Should be 0-127")

def main():
    pass

def create_port_callback(port_name, function):
    midiin, port_name = rtmidi.midiutil.open_midiinput(get_full_port_name(port_name, True))
    midiin.set_callback(function)



def open_virtual_output_port(name=None):
    MidiOutput = rtmidi.MidiOut()
    available_ports = MidiOutput.get_ports()

    if available_ports:
        for i in range(len(available_ports)):
            if name:
                if name in available_ports[i]:
                    print (available_ports[i], " found, opening port")
                    MidiOutput.open_port(i)
                # else:
                #     print (i, "string not found")
    else:
        MidiOutput.open_virtual_port("My generic virtual output")
    return MidiOutput


if __name__ == "__main__":
    main()
