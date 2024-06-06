class Grid:
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

    def __call__(self, x, y):
        if y <= self.rows and x <= self.columns:
            self.buttons[x, y]()

    def __getitem__(self, key):
        return self.buttons[key]


class Button:
    def __init__(self, x, y):
        self._state = False  # state is pressed or not
        self.pos = (x,y)
        self._action = None
        self._params = None
        self.num_actions = 0
        # self.assign_action(print)

    @property
    def state(self):
        pressed = "pressed." if self._state == True else "unpressed"
        print(self.pos, "is currently", pressed)
        return self._state

    @state.setter
    def state(self, value):
        pressed = "pressed." if self._state == True else "unpressed"
        print(self.pos, "has been", pressed)
        if self._state != value:
            self._state = value
        else:
            raise ValueError("This is a redundant button-press")

    def assign_action(self, function, params=None):
        if self.num_actions == 0:
            print("assigning function")
            self._action = function
        if self.num_actions == 0:
            self._params = params
        self.num_actions = 1


    def __call__(self, *args, **kwargs):
        print ("On the button")
        if self.num_actions == 1:
            # params = self._params[0] if len(self._params) > 0 else None
            self._action(self._params) #(self._params[0])
        # elif self.num_actions > 1:
        #     for i in range(len(self._action)):
        #         self._action[i](self._params[i])
        #         pass
        else:
            print("No assigned actions for button", self.pos)


    def __del__(self):
        if self._action:
            self._action = None
            print (f"actions for {self.pos} deleted")

    def append_action(self, function):
        pass

    def __str__(self):
        pressed = "pressed" if self._state else "not pressed"
        print (f"Button {self.pos} is curently {pressed}")

