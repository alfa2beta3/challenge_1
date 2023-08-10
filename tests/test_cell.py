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
                self.assertTrue(active_test_cell.future_state,
                                f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(active_test_cell.future_state,
                                 f'future_state should be false for {neighbor_count} neighbors')

        # Inactive cells should only be activated if they have exactly 3 neighbors
        inactive_test_cell = Cell((0, 0), (0, 0), active=False)
        for neighbor_count in range(9):
            inactive_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 3:
                self.assertTrue(inactive_test_cell.future_state,
                                f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(inactive_test_cell.future_state,
                                 f'future_state should be false for {neighbor_count} neighbors')

    def test_update(self):

        # Scenario 1: the inactive cell is updated to be active
        inactive_cell = Cell((0, 0), (0, 0))
        self.assertFalse(inactive_cell.active, 'the cell should be inactive initially')

        inactive_cell.future_state = True
        inactive_cell.update()
        self.assertTrue(inactive_cell.active, 'future state was set to true so the cell should become active')
        self.assertIs(inactive_cell.future_state, None, 'future state should be reset after the cell has been updated')

        # Scenario 2: the active cell is updated to be inactive
        active_cell = Cell((0, 0), (0, 0), True)
        self.assertTrue(active_cell.active, 'the cell should be active initially')

        active_cell.future_state = False
        active_cell.update()
        self.assertFalse(active_cell.active, 'future state was set to false so the cell should become inactive')
        self.assertIs(inactive_cell.future_state, None, 'future state should be reset after the cell has been updated')

    def test_flip(self):
        # test the flip method of the cell class

        # Scenario 1: set the inactive cell active
        inactive_cell = Cell((0, 0), (0, 0), active=False)
        inactive_cell.flip()
        self.assertTrue(inactive_cell.active, 'the inactive cell is flip, so cell should become active')

        # Scenario 2: set the active cell inactive
        active_cell = Cell((0, 0), (0, 0), active=True)
        active_cell.flip()
        self.assertFalse(active_cell.active, 'the active cell is flip, so cell should become inactive')
