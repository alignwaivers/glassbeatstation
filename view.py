class GridView:
    def __init__(self, model):
        self.model = model

    def __getitem__(self, key):
        return self.model.grid[key]

    def __str__(self):
        rows, columns = self.model.rows, self.model.columns
        console_grid = "\n"
        for col in range(columns):
            for row in range(rows):
                console_grid += "[X] " if self.model[row, col]._state == True else "[ ] "
            console_grid += "\n"
        return console_grid

# def action(self, *args):
#     if not args:
#         raise ValueError("no value for call press button: should be bool")
#     else:
#         press = args[0]
#         self.state = press
#         actions, params = self.get_actions(press)
#
#         # Check for actions
#         if len(actions) > 0:
#             for i in range(len(actions)):
#                 if params[i] is not None:
#                     try:
#                         if isinstance(params[i], str) or isinstance(params[i], int):
#                             actions[i](params[i])
#                         else:
#                             actions[i](*params[i])
#                     except:
#                         print("Error on button call", self.pos, actions[i], params[i])
#                 else:
#                     actions[i]()
#         else:
#             print("No assigned actions for button", self.pos, "when ", press)

    # def display(self):
    #     grid_str = self.grid_str
    #     for y in range(self.rows):
    #         for x in range(self.columns):
    #             if self.buttons[(x, y)]._state:
    #                 grid_str += "X "
    #             elif not self.buttons[(x, y)]._state:
    #                 grid_str += "0 "
    #         grid_str += '\n'
    #     return grid_str

    # def get_actions(self, press: bool, display=False):
    #     if press:
    #         actions = self._press_actions
    #         params = self._press_params
    #     else:
    #         actions = self._release_actions
    #         params = self._release_params
    #     if display == True:
    #         print(self.pos, press)
    #         for i in range(len(actions)):
    #             print(f"\n\tAction {i}: {actions[i]} "
    #                   f"\n\tParameters {i}: {params[i]}")
    #     return actions, params

    # def append_release_action(self, function, new_params):
    #     self.append_action(function, new_params, False)
    #
    # def append_action(self, function: object, new_params: list, press=True):
    #     actions, params = self.get_actions(press)
    #     if len(params) != len(actions):
    #         raise RuntimeError(f"Unmatched number of \nActions ({len(params)}) \nParameters ({len(params)})")
    #     if len(actions) == 0:
    #         # print(self.pos, press, "- Assigning  single function to button press:")
    #         actions.append(function)
    #         params.append(new_params)
    #         # print("\tAction:", self._press_actions, "\n\tParameters:", self._press_params)
    #         if len(params) > 1:
    #             raise IndexError("There are too many parameters")
    #         if len(actions) > 1:
    #             raise IndexError("There are too many actions")
    #     else:
    #         actions.append(function)
    #         params.append(new_params)
    #         print(self.pos, press, "now has an additional function")
    #         print("\tAction:", function, "\n\tParameters:", new_params)
