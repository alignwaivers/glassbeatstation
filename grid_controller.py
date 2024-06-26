class GridController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def midi_to_grid_mapping(self, *args):
        channel, note, vel = args[0]
        x = note % 16
        y = int(note / 16)
        toggle = "released :" if vel == 0 else "pressed :"
        print (f"Mode {self.model.mode} Button {x, y} {toggle} note={note}, velocity={vel}")
        press = True if vel == 127 else False
        self.handle_input(press, x, y)

    def handle_input(self, press, x, y):
        self.model.state = press
        self.view[x, y].action(press)
