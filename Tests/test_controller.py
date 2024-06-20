import unittest
from unittest.mock import patch
from io import StringIO

import sys
import os
import unittest

# Add the parent directory to sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


from grid_model import Grid
from grid_view import GridView
from grid_controller import GridController

class TestButtonGridController(unittest.TestCase):
    def setUp(self):
        self.model = Grid(3, 3)
        self.view = GridView(self.model)
        self.controller = GridController(self.model, self.view)

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_input(self, mock_stdout):
        self.controller.handle_input(0, 0)
        output = mock_stdout.getvalue().strip()
        self.assertIn("Button at (0, 0) has been activated in mode default.", output)
        self.assertIn("[X] [ ] [ ]\n[ ] [ ] [ ]\n[ ] [ ] [ ]", output)

    def test_set_mode(self):
        self.controller.set_mode(0)
        self.assertEqual(self.model.current_mode, 0)

if __name__ == '__main__':
    unittest.main()
