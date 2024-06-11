
class Grid:  # create midiversion and osc version? maybe should be inherit from genric Trigger
    def __init__(self, rows, columns):
        self.buttons = {}
        self.rows = rows
        self.columns = columns
        self.grid_str = ""
        for y in range(rows):
            for x in range(columns):
                self.buttons[(x, y)] = (Button(x, y, self))

    def __len__(self):
        return list(self.buttons.keys())

    def assign_range(self, function: object, new_params: list, rows, columns, press):
        for y in range(rows):
            for x in range(columns):
                if press:
                    self[x, y].append_action(function, new_params)
                else:
                    self[x, y].append_release_action(function, new_params)

    def display(self):
        grid_str = self.grid_str
        for y in range(self.rows):
            for x in range(self.columns):
                if self.buttons[(x, y)]._state:
                    grid_str += "X "
                elif not self.buttons[(x, y)]._state:
                    grid_str += "0 "
            grid_str += '\n'
        return grid_str

    def send_midi_message(self, midi_device, note=60, velocity=127, channel=0x90):
        if 0 <= velocity <= 127 and 0 <= note <= 127:
            message = [channel, note, velocity]  # channel 1, middle C, velocity 112
            midi_device.midi_out.send_message(message)
        else:
            raise ValueError(f"velocity({velocity}) or note({note}) is out of range for midi message. Should be 0-127")

    def print_num_functions(self, press):
        grid_str = ""
        for y in range(self.rows):
            for x in range(self.columns):
                actions, _params = self.buttons[x, y].get_actions(press)
                grid_str += str(len(actions)) + " "
            grid_str += '\n'
        print(grid_str)

    def __getitem__(self, key):
        return self.buttons[key]


class Button:
    def __init__(self, x, y, Grid):
        self._state = False  # state is pressed or not
        self.pos = (x, y)
        self._press_actions = [] # create actions/execution class?
        self._press_params = []
        self._release_actions = []
        self._release_params = []
        self.Grid = Grid

    def __len__(self):
        return len(self._press_actions)
    def get_actions(self, press: bool, display=False):
        if press:
            actions = self._press_actions
            params = self._press_params
        else:
            actions = self._release_actions
            params = self._release_params
        if display==True:
            print (self.pos, press)
            for i in range(len(actions)):
                print (f"\n\tAction {i}: {actions[i]} "
                       f"\n\tParameters {i}: {params[i]}")
        return actions, params

    def append_release_action(self, function, new_params):
        self.append_action(function, new_params, False)

    def append_action(self, function: object, new_params: list, press=True):
        actions, params = self.get_actions(press)
        if len(params) != len(actions):
            raise RuntimeError(f"Unmatched number of \nActions ({len(params)}) \nParameters ({len(params)})")
        if len(actions) == 0:
            # print(self.pos, press, "- Assigning  single function to button press:")
            actions.append(function)
            params.append(new_params)
            # print("\tAction:", self._press_actions, "\n\tParameters:", self._press_params)
            if len(params) > 1:
                raise IndexError("There are too many parameters")
            if len(actions) > 1:
                raise IndexError("There are too many actions")
        else:
            actions.append(function)
            params.append(new_params)
            print(self.pos, press, "now has an additional function")
            print("\tAction:", function, "\n\tParameters:", new_params)

    def action(self, *args):
        if not args: raise ValueError("no value for call press button: should be bool")
        else:
            press = args[0]
            self.state = press
            actions, params = self.get_actions(press)

            # Check for actions
            if len(actions) > 0:
                for i in range(len(actions)):
                    if params[i] is not None:
                        try:
                            if isinstance(params[i], str) or isinstance(params[i], int):
                                actions[i](params[i])
                            else:
                                actions[i](*params[i])
                        except:
                            print ("Error on button call", self.pos,  actions[i], params[i])
                    else:
                        actions[i]()
            else:
                print("No assigned actions for button", self.pos, "when ", press)


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value:bool):
        if self._state != value:
            self._state = value
        else:
            raise ValueError("This is a redundant button-press")