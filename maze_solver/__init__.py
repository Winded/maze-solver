from maze_solver.data_structures import SolvedMaze
from . import text_format, pathfinder

def solve(maze_input: str, max_path_length: int = 200) -> SolvedMaze:
    """
    Parse the given input maze string and find the shortest paths for the closest exit point
    for each entry point.

    max_path_length determines the maximum amount of moves that can be made when resolving a path.
    If the resulting path gets any longer than this value, an empty path (meaning: no solution)
    will be returned.
    """

    maze = text_format.parse(maze_input)
    paths = pathfinder.find_shortest_paths_for_maze(maze, max_path_length)

    return SolvedMaze(maze, paths)


def print_solutions(solved_maze: SolvedMaze) -> None:
    """
    Print given solved maze to standard output.
    """
    for path in solved_maze.paths:
        print(text_format.render(solved_maze.maze.grid, path))
        if len(path) > 0:
            print('Total Moves: %i\n' % len(path))
        else:
            print('No solution\n')
