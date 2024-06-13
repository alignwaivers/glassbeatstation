class GridView:
    def __init__(self, model):
        self.model = model
        self.buttons = {}
        self.arguments = {}
        for button in model.buttons.keys():
            self.buttons[button] = Button(button[0], button[1])


        self[0,0].action()
        self[0,0].release()


    def __getitem__(self, key):
        return self.buttons[key]

class Button:
    def __init__(self, col, row):
        self._actions = {True: [], False: []}
        self._arguments = {True: [], False: []}
        self.row = row
        self.col = col

    def set_release(self, action, arguments):
        self.set_action(action, arguments, press=False)


    def set_action(self, action, arguments, press=True):
        self._actions[press].append(action)
        self._arguments[press].append(arguments)

    def release(self):
        self.action(press=False)

    def action(self, press=True):
        actions = self._actions[press]
        arguments = self._arguments[press]
        if len(arguments) > 0:
            for i in range(len(actions)):
                if isinstance(arguments[i], list):
                    actions[i](*arguments[i])
                else:
                    actions[i](arguments[i])



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
