from collections import OrderedDict


class Looper():
    def __init__(self, num_loops, osc_out, return_port):
        self.num_loops = num_loops
        self.osc_out = osc_out
        self.loops = [Loop(str(i), osc_out, return_port) for i in range(num_loops)]

    def __getitem__(self, key):
        return self.loops[key]

    def handle_input(self, *args):
        prefix, loop_num, command, value = args[0], args[1], args[2], args[3::]
        print (args)
        loop = self.loops[loop_num]#
        # TODO handle dependency actions based on grid mode
        if command == "state":
            loop.update_state(int(value[0]))
        elif command == "loop_pos":
            loop.update_pos(value[0])
        elif command == "loop_len":
            loop.update_len(value[0])
class Loop():
    def __init__(self, index, osc_out, return_port, interval=10):
        print ("Loop #{} created".format(index))
        self.osc_out = osc_out
        self.loop_idx = index
        self.state = "paused"
        self.length = None
        self.position = None
        self.states_dict = OrderedDict([("Off", 0),
                                ("WaitStart", 28),
                                ("Recording", 7),
                                 ("WaitStop", 28),
                                 ("Playing", 62),
                                ("Overdubbing", 40),
                                 ("Multiplying", 63)])
        #                          ("Inserting", 0),
        #                          ("Replacing", 0),
        #                         ("Delay", 0),
        #                          ("Muted", 10),  # 10
        #                           ("Scratching", 0),
        #                            ("OneShot", 0),
        #                             ("Subsitute", 0),
        #                              ("Paused", 0)])
        self.states_list = list(self.states_dict.keys())



        '''
        Off: MIDI note value 0
        Red (low): MIDI note value 13
        Red (medium): MIDI note value 15
        Red (high): MIDI note value 7
        Green (low): MIDI note value 28
        Green (medium): MIDI note value 60
        Green (high): MIDI note value 62
        Amber (low): MIDI note value 29
        Amber (medium): MIDI note value 63
        Amber (high): MIDI note value 127
        Yellow (medium): MIDI note value 30
        Yellow (high): MIDI note value 31
        Orange: MIDI note value 127
        Lime: MIDI note value 126
        Light Green: MIDI note value 125
        Extended Colors
        Dark Red: MIDI note value 5
        Dark Green: MIDI note value 16
        Dark Amber: MIDI note value 37
        Bright Red: MIDI note value 72
        Bright Green: MIDI note value 122
        Bright Amber: MIDI note value 123
        '''

        osc_out.send("/sl/{}/register_auto_update".format(index),
                 ["state", interval, "localhost:"+return_port, "/sloop"])
        osc_out.send("/sl/{}/register_auto_update".format(index),
                 ["loop_len", interval, "localhost:"+return_port, "/sloop"])
        osc_out.send("/sl/{}/register_auto_update".format(index),
                 ["loop_pos", interval, "localhost:"+return_port,"/sloop"])

    def loop_action(self, action):
        print ("/sl/{}/down".format(self.loop_idx), action)
        self.osc_out.send("/sl/{}/down".format(self.loop_idx), action)


    # The following "update" methods have been routed via OSC messages from sooperlooper
    def update_len(self, length):
        if length != self.length:
            self.length = length
        else:
            raise ValueError("Redundant length not updated")

    def update_pos(self, position):
        if position != self.position:
            self.position = position
        else:
            raise ValueError("Redundant position not updated")

    def update_state(self, state_num):
        new_state = self.states_list[state_num]
        if new_state != self.state:
            self.state = self.states_list[state_num]
            print("Loop #{} is {}".format(self.loop_idx, new_state))

        else:
            raise ValueError("Redundant state change not updated")

