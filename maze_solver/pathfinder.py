import sys
from maze_solver.data_structures import Grid, Maze, Point


def find_shortest_paths_for_maze(maze: Maze) -> 'list[list[Point]]':
    """
    Finds the shortest exit paths for each start point in the given maze.
    """
    
    result_paths = []
    for start_point in maze.start_points:
        result_paths.append(find_shortest_path_to_closest_exit(start_point, maze.end_points, maze.grid))
    
    return result_paths


def find_shortest_path_to_closest_exit(start_point: Point, exit_points: 'list[Point]', grid: Grid) -> 'list[Point]':
    """
    Finds the shortest paths from start point to all given exit points, and selects the shortest of these paths.
    """
    if len(exit_points) == 0:
        raise ValueError(exit_points)

    chosen_path = None
    for exit_point in exit_points:
        path = find_shortest_path(start_point, exit_point, grid)
        if chosen_path == None or len(path) < len(chosen_path):
            chosen_path = path

    return chosen_path


def find_shortest_path(start_point: Point, end_point: Point, grid: Grid) -> 'list[Point]':
    """
    Finds the shortest path from given start point in grid to given end point.

    Returns an empty path if there is no solution.
    """

    def reconstruct_path(came_from: 'dict[Point, Point]', current: Point) -> 'list[Point]':
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path

    def heuristic(point: Point):
        return abs(end_point.x - point.x) + abs(end_point.y - point.y)

    # Dictionary of Point -> bool, representing currently discovered passable cells
    # which we want to travel to. start_point is discovered by default
    open_set = {
        start_point: True,
    }
    # A mapping of Point in the current cheapest path to the previous Point preceding it
    came_from = {}

    # Dictionary of Point -> int
    # Cost of the currently known shortest path from start point to key cell
    # If cell is not in dict, the cost for that cell should be considered infinite
    g_score = {
        start_point: 0,
    }
    # Dictionary of Point -> int
    # Estimated cost of path if it goes through the given cell
    # Calculated as f_score[n] = g_score[n] + heuristic(n)
    f_score = {
        start_point: heuristic(start_point)
    }

    # Loop until open_set is empty
    while open_set:
        # Find current cell, which is the cell with the lowest f_score in the open set
        current_cell = None
        current_score = sys.maxsize
        for cell in open_set:
            if f_score[cell] < current_score:
                current_cell = cell
                current_score = f_score[cell]

        # If current cell is the same as end point, we have solved the maze
        # Reconstruct the path by walking through came_from dictionary, startin with current cell
        if current_cell == end_point:
            return reconstruct_path(came_from, current_cell)

        # Remove current cell from open set
        open_set.pop(current_cell)

        neighbors = grid.get_passable_neighbor_cells(current_cell)
        for neighbor in neighbors:
            # Tentative gscore is the cost of moving from start cell to current cell through this neighboring cell
            # The cost of moving to a neighboring cell is 1
            tentative_gscore = g_score[current_cell] + 1 if current_cell in g_score else sys.maxsize
            if tentative_gscore < (g_score[neighbor] if neighbor in g_score else sys.maxsize):
                # This path is lower-cost than the currently cheapest path to neighbor.
                # Override this as the cheapest path
                came_from[neighbor] = current_cell
                g_score[neighbor] = tentative_gscore
                f_score[neighbor] = tentative_gscore + heuristic(neighbor)
                if neighbor not in open_set:
                    open_set[neighbor] = True

    # open_set is empty but end point was never reached: there is no solution
    return []
