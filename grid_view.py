class GridView:
    def __init__(self, model, midi_output):
        self.model = model
        self.midi_output = midi_output

    def __getitem__(self, key):
        return self.model.grid[key]

    def display_console(self):
        rows, columns = self.model.rows, self.model.columns
        console_grid = "\n"
        for col in range(columns):
            for row in range(rows):
                console_grid += "[X] " if self.model[row, col]._state == True else "[ ] "
            console_grid += "\n"
        return console_grid

    def release_leds(self):
        for col in range(self.model.columns - 1):
            for row in range(self.model.rows - 1):
                self.midi_output.send_messages(row + col*16, 0)

    def set_mode(self, mode):
        if self.model.mode != mode:
            print (f"Mode changing from {self.model.mode} to {mode}")
            self.model.mode = mode
        else:
            print(f"Remaining in mode {self.model.mode}")

    def map_to_midi(self, x, y):
        return x + y*16

    def switch_mode(self, mode):
         if self.model.mode != mode: # could implement the difference of clrs only here
            self.model.mode = mode
            for button in self.model.grid.keys():
                self.midi_output.send_messages(button.note, button.clr[mode])
         else:
            print(f"Mode unchanged: Already in mode {mode}")


