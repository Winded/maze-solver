import unittest
from maze_solver.data_structures import Grid, Point
from maze_solver.pathfinder import find_shortest_path


class TestFindShortestPath(unittest.TestCase):
    """
    Unit test cases for function: pathfinder.find_shortest_path

    The algorithm is tested both with pre-determined and generated maze grids, start points and exit points.
    """

    def perform_path_test(self, start_point: Point, end_point: Point, grid: Grid, expect_success: bool):
        path = find_shortest_path(start_point, end_point, grid)
        if expect_success:
            self.assertNotEqual(len(path), 0)
        else:
            self.assertEqual(len(path), 0)

    def test_valid_mazes(self):
        # Test a grid where all cells are passable
        grid = Grid(10, 10, [True] * 100)
        start_point = Point(4, 4)
        end_point = Point(6, 8)
        self.perform_path_test(start_point, end_point, grid, True)

        # Test a grid where every other cell is passable
        passability = [True] * 100
        for x in range(0, 10, 2):
            for y in range(0, 10, 2):
                passability[y * 10 + x] = False
        grid = Grid(10, 10, passability)
        start_point = Point(3, 4)
        end_point = Point(5, 9)
        self.perform_path_test(start_point, end_point, grid, True)

    def test_invalid_mazes(self):
        # Test a grid where there is a linear wall between start and end
        passability = [True] * 100
        for x in range(0, 10):
            passability[1 * 10 + x] = False
        grid = Grid(10, 10, passability)
        start_point = Point(5, 0)
        end_point = Point(5, 5)
        self.perform_path_test(start_point, end_point, grid, False)

        # Test a grid where there is a diagonal line accross the center
        passability = [True] * 100
        for x in range(0, 10):
            passability[x * 10 + x] = False
        grid = Grid(10, 10, passability)
        start_point = Point(5, 0)
        end_point = Point(5, 7)
        self.perform_path_test(start_point, end_point, grid, False)
