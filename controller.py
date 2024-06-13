class GridController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def midi_to_grid_mapping(self, *args):
        print ("button pressed :", args[0])
        channel, note, vel = args[0]
        x = note % 16
        y = int(note / 16)
        press = True if vel == 127 else False
        self.view[x, y].action(press)