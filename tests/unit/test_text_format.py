from maze_solver.data_structures import Point
import maze_solver.text_format as text_format
import unittest


valid_input = """#E#
# #
#^#
"""


invalid_inputs = [
"""
#E#
# #
#J 
""",
"""
#E
# #
#
""",
"""
#E
# X 
#
""",
]


class TestParse(unittest.TestCase):
    """
    Unit test cases for function: text_format.parse
    """

    def test_parse_valid_input(self):
        maze = text_format.parse(valid_input)
        self.assertEqual(maze.start_points, [Point(1, 2)])
        self.assertEqual(maze.end_points, [Point(1, 0)])
        self.assertEqual(maze.grid.width, 3)
        self.assertEqual(maze.grid.height, 3)
        self.assertTrue(maze.grid.is_passable(Point(1, 1)))
        self.assertFalse(maze.grid.is_passable(Point(0, 1)))

    def test_parse_invalid_inputs(self):
        for invalid_input in invalid_inputs:
            self.assertRaises(text_format.ParseError, lambda: text_format.parse(invalid_input))


class TestRender(unittest.TestCase):
    """
    Unit test cases for function: text_format.render
    """
    pass
