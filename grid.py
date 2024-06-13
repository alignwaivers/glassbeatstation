
class Grid:
    def __init__(self, rows, columns):
        self.grid = {}
        self.rows = rows
        self.columns = columns

        for y in range(rows):
            for x in range(columns):
                self.grid[(x, y)] = Button(x, y)

    def __getitem__(self, key):
        return self.grid[key]

class Button:
    def __init__(self, col, row):
        self._state = False
        self._actions = {True: [], False: []}
        self._arguments = {True: [], False: []}
        self.row = row
        self.col = col

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value:bool):
        if self._state != value:
            self._state = value
        else:
            raise ValueError("This is a redundant button-press")
    def set_release(self, action, arguments):
        self.set_action(action, arguments, press=False)

    def set_action(self, action, arguments, press=True):
        self._actions[press].append(action)
        self._arguments[press].append(arguments)


    def release(self):
        self.action(press=False)

    def action(self, press=True):
        # button = self.
        self.state = press
        actions = self._actions[press]
        arguments = self._arguments[press]
        if len(arguments) > 0:
            for i in range(len(actions)):
                if isinstance(arguments[i], list):
                    actions[i](*arguments[i])
                else:
                    actions[i](arguments[i])


    # def assign_range(self, function: object, new_params: list, rows, columns, press):
    #     for y in range(rows):
    #         for x in range(columns):
    #             if press:
    #                 self[x, y].append_action(function, new_params)
    #             else:
    #                 self[x, y].append_release_action(function, new_params)
