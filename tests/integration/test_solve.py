import unittest
from .data import mazes
import maze_solver


class TestSolve(unittest.TestCase):
    """
    Test maze_solver.solve function with "real" maze input data.
    """

    def perform_solve(self, max_path_length: int):
        for maze in mazes:
            result = maze_solver.solve(maze, max_path_length)
            for path in result.paths:
                self.assertLessEqual(len(path), max_path_length)

    def test_solve_less_or_equal_200(self):
        self.perform_solve(200)

    def test_solve_less_or_equal_150(self):
        self.perform_solve(150)

    def test_solve_less_or_equal_20(self):
        self.perform_solve(20)
