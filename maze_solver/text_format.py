"""
Functions for parsing from, and rendering into, the maze text format.

Maze text format constructs a Grid with fixed-size width and height.
The maze can include impassable cells, passable cells, starting points
and exit points.

The allowed characters in the maze file are:
 - `#`, which will represent a block, or wall (unmovable space)
 - ` ` (single empty space), which will represent a movable space
 - `^`, which is a starting point and
 - `E`, which is an exit point
"""

from .data_structures import Grid, Maze, Point


allowed_characters = ('#', ' ', '^', 'E')


class ParseError(Exception):
    pass


def parse(input: str) -> Maze:
    """
    Parse a maze string into a Maze object.
    """

    # Calling strip removes trailing whitespace if the input is from a text file
    lines = input.strip().split('\n')
    height = len(lines)
    if height == 0:
        raise ParseError('Input string is empty')
    width = len(lines[0])

    start_points = []
    end_points = []
    passability = []

    for line_number, line in enumerate(lines):
        if len(line) != width:
            raise ParseError('Line #%i has wrong length (Expected %i, found %i)' % (
                line_number, width, len(line)))

        for char_number, char in enumerate(line):
            if char not in allowed_characters:
                raise ParseError('Unrecognized character "%c" at line %i column %i' % (
                    char, line_number, char_number))

            if char == '#':
                passability.append(False)
            else:
                passability.append(True)

            if char == '^':
                start_points.append(Point(char_number, line_number))
            elif char == 'E':
                end_points.append(Point(char_number, line_number))

    return Maze(Grid(width, height, passability), start_points, end_points)


def render(grid: Grid, path: 'list[Point]') -> str:
    """
    Render the given grid and path solution to text.
    """

    # Apply path to a dict used to override characters when looping through the grid
    grid_override = {}
    if len(path) > 0:
        for point_index in range(1, len(path)):
            point = path[point_index]
            previous_point = path[point_index - 1]
            
            if point.x < previous_point.x:
                grid_override[previous_point] = '<'
            elif point.x > previous_point.x:
                grid_override[previous_point] = '>'

            if point.y < previous_point.y:
                grid_override[previous_point] = '^'
            elif point.y > previous_point.y:
                grid_override[previous_point] = 'V'
        grid_override[path[0]] = 'S'
        grid_override[path[-1]] = 'E'

    result = ''
    for y in range(grid.height):
        for x in range(grid.width):
            point = Point(x, y)
            if point in grid_override:
                result += grid_override[point]
            else:
                result += ' ' if grid.is_passable(point) else '#'
        result += '\n'

    return result
