
class Grid:
    def __init__(self, rows, columns, num_modes=1):
        self.num_modes = num_modes
        self.mode = 0 # default mode
        self.grid = {} # collection of button objects
        self.rows = rows
        self.columns = columns

        
        for y in range(rows):
            for x in range(columns):
                self.grid[(x, y)] = Button(x, y, self)

    def __getitem__(self, key):
        return self.grid[key]


class Button:
    def __init__(self, col, row, grid):
        self.Grid = grid
        self._state = False
        self._actions = [{True: [], False: []} for mode in range(grid.num_modes)]
        self._arguments = [{True: [], False: []} for mode in range(grid.num_modes)]
        self.row = row
        self.col = col
        # self.clr_stack = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value:bool):
        if self._state != value:
            self._state = value
        else:
            print("This is a redundant button-press")

    def set_release(self, action, arguments, mode:int = 0):
        self.set_action(action, arguments, mode, press=False)

    def set_action(self, action, arguments, mode:int = 0, press=True):
        self._actions[mode][press].append(action)
        self._arguments[mode][press].append(arguments)


    def release(self, mode:int = 0):
        self.action(press=False)

    def action(self, press=True):
        mode = self.Grid.mode
        actions = self._actions[mode][press]
        arguments = self._arguments[mode][press]
        if len(actions) != len(arguments):
            raise IndexError("Invalid number of actions", len(actions), "to arguments", len(arguments))
        if len(arguments) > 0:
            for i in range(len(actions)):
                if isinstance(arguments[i], list):
                    actions[i](*arguments[i])
                else:
                    actions[i](arguments[i])


