from argparse import ArgumentError
from collections import namedtuple
from decimal import InvalidOperation


class GridDimensionsError(Exception):
    pass


class InvalidPointError(Exception):
    pass


class Point(namedtuple('Point', ['x', 'y'])):
    """
    Point is a two-dimensional vector referencing a cell in the maze grid.
    """
    pass


class Grid:
    """
    The Grid class is a data-class providing the structure for maze grids.

    A maze grid consists of passable and impassable cells. Thus, the internal
    structure is a dictionary that uses Point as a key, and bool as a value.
    True means passable, False means impassable.
    """

    def __init__(self, width: int, height: int, passability_values: 'list[bool]') -> None:
        self._width = width
        self._height = height
        self._passability = {}

        if len(passability_values) != width * height:
            raise GridDimensionsError(
                'Dimensions do not match length of passable_values list')

        x = 0
        y = 0
        for passable in passability_values:
            assert x < width, y < height
            self._passability[Point(x, y)] = passable
            x += 1
            if x >= width:
                x = 0
                y += 1

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def is_point_in_grid(self, point: Point) -> bool:
        """
        Returns True if the given point is within the bounds of the grid, False otherwise.
        """
        return point.x >= 0 and point.x < self._width and point.y >= 0 and point.y < self._height

    def is_passable(self, point: Point) -> bool:
        if point not in self._passability:
            raise InvalidPointError(
                'Invalid or out-of-bounds point given: (%i, %i)' % point)
        return self._passability[point]

    def get_passable_neighbor_cells(self, cell: Point) -> 'tuple[Point]':
        """
        Returns a tuple of cell points that are passable neighbors of given cell.
        """

        # Calculate neighboring coordinates
        neighbors = (
            Point(cell.x - 1, cell.y - 1),
            Point(cell.x, cell.y - 1),
            Point(cell.x + 1, cell.y - 1),
            Point(cell.x - 1, cell.y),
            Point(cell.x + 1, cell.y),
            Point(cell.x - 1, cell.y + 1),
            Point(cell.x, cell.y + 1),
            Point(cell.x + 1, cell.y + 1),
        )

        # Then filter coordinates that are out-of-bounds or impassable
        return tuple(filter(lambda neighbor: self.is_point_in_grid(neighbor) and self.is_passable(neighbor), neighbors))
