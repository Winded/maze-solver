from argparse import ArgumentError
from timeit import repeat
from maze_solver.data_structures import Grid, GridDimensionsError, InvalidPointError, Point
import unittest

class TestGrid(unittest.TestCase):
    """
    Unit test cases for the Grid class.

    Validates that the constructor and public methods are working as expected.
    """

    def setUp(self):
        width = 10
        height = 10
        passability = [True] * (width * height)
        self.impassable_points = [Point(3, 4), Point(6, 5), Point(0, 9)]
        for impassable in self.impassable_points:
            passability[impassable.y * width + impassable.x] = False
        self.grid = Grid(width, height, passability)

    def test_init_invalid_dimensions(self):
        self.assertRaises(GridDimensionsError, lambda: Grid(20, 10, [True, False]))
        self.assertRaises(GridDimensionsError, lambda: Grid(5, 5, [True] * 50))
        self.assertRaises(GridDimensionsError, lambda: Grid(-4, 2, []))

    def test_width_property(self):
        self.assertEqual(self.grid.width, 10)

    def test_height_property(self):
        self.assertEqual(self.grid.height, 10)

    def test_passable_method(self):
        self.assertTrue(self.grid.is_passable(Point(3, 2)))
        self.assertTrue(self.grid.is_passable(Point(4, 5)))
        self.assertTrue(self.grid.is_passable(Point(9, 9)))

        self.assertFalse(self.grid.is_passable(Point(3, 4)))
        self.assertFalse(self.grid.is_passable(Point(6, 5)))
        self.assertFalse(self.grid.is_passable(Point(0, 9)))

    def test_passable_method_invalid_point(self):
        self.assertRaises(InvalidPointError, lambda: self.grid.is_passable(Point(10, 10)))
        self.assertRaises(InvalidPointError, lambda: self.grid.is_passable(Point(5, 15)))
        self.assertRaises(InvalidPointError, lambda: self.grid.is_passable(Point(-3, 4)))

    def test_get_passable_neighbor_cells(self):
        self.assertEqual(self.grid.get_passable_neighbor_cells(Point(0, 8)), (
            Point(0, 7),
            Point(1, 8),
        ))
