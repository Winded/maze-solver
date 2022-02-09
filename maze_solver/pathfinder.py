"""

1. Mark start point as visited and push it to path
2. Start path search loop
3. Return path array, which is empty if there is no solution

Path search loop:
1. If current cell is an exit cell, STOP
2. Get neighboring empty and non-visited cells of current cell
3. Branch based on neighboring cells
  a. One or more neighboring cells: move to first cell, add to visited cells and path, GOTO 1
  b. No neighboring cells: Remove latest element from path and set it as current cell, GOTO 1
  c. No neighboring cells, and path array is empty: STOP

"""

def find_shortest_path(start_point, end_points, grid):
    pass
