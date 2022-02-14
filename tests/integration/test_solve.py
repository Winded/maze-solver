import unittest
from .data import mazes
import maze_solver


class TestSolve(unittest.TestCase):
    """
    Test maze_solver.solve function with "real" maze input data.
    """

    def perform_solve(self, max_path_length: int, expected_results: 'list[bool]'):
        for i, maze in enumerate(mazes):
            result = maze_solver.solve(maze)
            for path in result.paths:
                self.assertEqual(len(path) <= max_path_length, expected_results[i])

    def test_solve_less_or_equal_200(self):
        self.perform_solve(200, [True, True])

    def test_solve_less_or_equal_150(self):
        self.perform_solve(150, [True, False])

    def test_solve_less_or_equal_20(self):
        self.perform_solve(20, [False, False])
