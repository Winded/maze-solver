from maze_solver.data_structures import Grid, Maze, Point


def find_shortest_paths_for_maze(maze: Maze, max_path_length: int) -> 'list[list[Point]]':
    """
    Finds the shortest exit paths for each start point in the given maze.
    """
    
    result_paths = []
    for start_point in maze.start_points:
        result_paths.append(find_shortest_path_to_closest_exit(start_point, maze.end_points, maze.grid, max_path_length))
    
    return result_paths


def find_shortest_path_to_closest_exit(start_point: Point, exit_points: 'list[Point]', grid: Grid, max_path_length: int) -> 'list[Point]':
    """
    Finds the shortest paths from start point to all given exit points, and selects the shortest of these paths.
    """
    if len(exit_points) == 0:
        raise ValueError(exit_points)

    chosen_path = None
    for exit_point in exit_points:
        path = find_shortest_path(start_point, exit_point, grid, max_path_length)
        if chosen_path == None or len(path) < len(chosen_path):
            chosen_path = path

    return chosen_path


def find_shortest_path(start_point: Point, end_point: Point, grid: Grid, max_path_length: int) -> 'list[Point]':
    """
    Finds the shortest path from given start point in grid to given end point.

    Returns an empty path if there is no solution, or if solution is longer than max_path_length.
    """

    # Keep track on currently built path and cells that have been visited
    path = []
    visited_cells = {}

    # Initial cell is the starting point, mark it as visited and push it to path
    current_cell = start_point
    path.append(current_cell)
    visited_cells[current_cell] = True

    keep_moving = True
    while keep_moving:
        if current_cell == end_point:
            keep_moving = False
            continue

        # Get passable non-visited neighboring cells
        neighbors = tuple(filter(
            lambda neighbor: neighbor not in visited_cells, grid.get_passable_neighbor_cells(current_cell)))

        if len(neighbors) > 0:
            # Move to first non-visited neighbor
            current_cell = neighbors[0]
            path.append(current_cell)
            visited_cells[current_cell] = True
        elif len(path) > 0:
            # Move back one cell in path
            current_cell = path.pop()
        else:
            # No passable non-visited neighbors and path is empty means there is no solution
            keep_moving = False

    if len(path) > max_path_length:
        return []

    return path
