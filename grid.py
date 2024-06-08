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
        for x in range(self.rows):
            for y in range(self.columns):
                if self.buttons[(x, y)]._state:
                    grid_str += "X "
                elif not self.buttons[(x, y)]._state:
                    grid_str += "0 "
            grid_str += '\n'
        return grid_str


    def __getitem__(self, key):
        return self.buttons[key]


class Button:
    def __init__(self, x, y):
        self._state = False  # state is pressed or not
        self.pos = (x,y)
        self._press_actions = [] # create actions/execution class?
        self._press_params = []
        self._release_actions = []
        self._release_params = []

    def get_actions(self, press: bool):
        if press:
            actions = self._press_actions
            params = self._press_params
        elif not press:
            actions = self._release_actions
            params = self._release_params
        return actions, params

    def assign_action(self, function, newparams, press:bool=True, override=False):
        actions, params = self.get_actions(press)
        params = self._press_params
        print (params)
        if len(actions) == 0 or override:
            print(self.pos, "Assigning  single function :", function)
            actions.append(function)
            params.append(newparams)
            print (self._press_actions, self._press_params)
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
            ## Check for actions
            if len(actions) > 0:
                for i in range(len(actions)):
                    actions[i](params[i])
            else:
                print("No assigned actions for button", self.pos)


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value:bool):
        if self._state != value:
            self._state = value
            # pressed = "pressed." if value else "unpressed"
            # print(self.pos, "has been", pressed)
        else:
            raise ValueError("This is a redundant button-press")


    # def __str__(self):
    #     pressed = "pressed" if self._state else "not pressed"
    #     print (f"Button {self.pos} is curently {pressed}")
    #     # print ("Press functions: ", [i for i in self._press_actions])
    #     # print ("Press functions: ", [i for i in self._release_actions])

