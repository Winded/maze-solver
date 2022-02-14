from maze_solver.data_structures import SolvedMaze
from . import text_format, pathfinder


def solve(maze_input: str) -> SolvedMaze:
    """
    Parse the given input maze string and find the shortest paths for the closest exit point
    for each entry point.
    """

    maze = text_format.parse(maze_input)
    paths = pathfinder.find_shortest_paths_for_maze(maze)

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
