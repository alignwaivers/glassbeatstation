class Grid: #create midiversion and osc version?
    def __init__(self, rows, columns):
        self.buttons = {}
        self.rows = rows
        self.columns = columns
        self.grid_str = ""
        for y in range(rows):
            for x in range(columns):
                self.buttons[(x, y)] = (Button(x, y))


    def __str__(self):
        grid_str = self.grid_str
        for y in range(self.rows):
            for x in range(self.columns):
                if self.buttons[(x, y)]._state:
                    grid_str += "X "
                elif not self.buttons[(x, y)]._state:
                    grid_str += "0 "
            grid_str += '\n'
        return grid_str

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
    def __init__(self, x, y):
        self._state = False  # state is pressed or not
        self.pos = (x, y)
        self._press_actions = [] # create actions/execution class?
        self._press_params = []
        self._release_actions = []
        self._release_params = []


    def get_actions(self, press: bool):
        if press == True:
            actions = self._press_actions
            params = self._press_params
        else:
            actions = self._release_actions
            params = self._release_params
        return actions, params

    def assign_action(self, function, newparams, press:bool=True, override=False):
        actions, params = self.get_actions(press)
        if len(params) != len(actions):
            raise RuntimeError(f"Unmatched number of \nActions ({len(params)}) \nParameters ({len(params)})")
        if len(actions) == 0 or override:
            print(self.pos, press, "- Assigning  single function :")
            actions.append(function)
            params.append(newparams)
            print ("\tAction:", self._press_actions, "\n\tParameters:", self._press_params)
            if len(params) > 1:
                raise IndexError("There are too many parameters")
            if len(actions) > 1:
                raise IndexError("There are too many actions")
        else:
            actions.append(function)
            params.append(newparams)
            print(self.pos, "now has an additional function")



    def __call__(self, *args):
        if not args: raise ValueError("no value for call press button: should be bool")
        else:
            press = args[0]
            self.state = press
            actions, params = self.get_actions(press)

            # Check for actions
            if len(actions) > 0:
                for i in range(len(actions)):
                    if params[i] != None:
                        actions[i](params[i])
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