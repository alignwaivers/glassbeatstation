
class Grid:  # create midiversion and osc version? maybe should be inherit from genric Trigger
    def __init__(self, rows, columns):
        self.buttons = {}
        self.rows = rows
        self.columns = columns
        self.grid_str = ""
        for y in range(rows):
            for x in range(columns):
                self.buttons[(x, y)] = False

    # def __len__(self):
    #     return list(self.buttons.keys())

    # def assign_range(self, function: object, new_params: list, rows, columns, press):
    #     for y in range(rows):
    #         for x in range(columns):
    #             if press:
    #                 self[x, y].append_action(function, new_params)
    #             else:
    #                 self[x, y].append_release_action(function, new_params)

    def __getitem__(self, key):
        return self.buttons[key]

#
# class Button:
#     def __init__(self, x, y, Grid):
#         self._state = False  # state is pressed or not
#         self.pos = (x, y)
#         self.Grid = Grid
#
#     @property
#     def state(self):
#         return self._state
#
#     @state.setter
#     def state(self, value:bool):
#         if self._state != value:
#             self._state = value
#         else:
#             raise ValueError("This is a redundant button-press")