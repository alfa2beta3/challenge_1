from unittest import TestCase
from cell import *


class TestCell(TestCase):
    def test_set_future_state(self):
        active_test_cell = Cell((0, 0), (0, 0), active=True)
        # neighbor count will have values from 0 to 8 inclusive.
        # This works because a cell can have 0 to 8 active neighbors

        # Active cells should only stay active if they have 2 or 3 neighbors
        for neighbor_count in range(9):
            active_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 2 or neighbor_count == 3:
                self.assertTrue(active_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(active_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

        # Inactive cells should only be activated if they have exactly 3 neighbors
        inactive_test_cell = Cell((0, 0), (0, 0), active=False)
        for neighbor_count in range(9):
            inactive_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 3:
                self.assertTrue(inactive_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(inactive_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

    def test_update(self):

        # Scenario 1: the cell's future state is inactive
        cell = Cell((0, 0), (0, 0))
        cell.future_state = False
        cell.update()
        self.assertFalse(cell.active)

        # Scenario 2: the cell is active
        cell.future_state = True
        cell.update()
        self.assertTrue(cell.active)

    def test_flip(self):
        # test the flip method of the cell class
        active_cell = Cell((0, 0), (0, 0), active=False)
        active_cell.flip()
        self.assertTrue(active_cell.active)
