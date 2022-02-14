# Maze solver

This Python application can solve a maze provided by the input text file.
Python 3.5 or higher is recommended. The application has been tested with Python 3.7.

## Running tests

You can run tests using the `unittest` module.

```sh
cd path-to-project/
python -m unittest discover -s tests/
```

## Installing

```sh
cd path-to-project/
pip install .
```

After installation, `maze-solver` script is in your PATH environment and you
can call the script from anywhere.

## Usage

To use the program, run it in the command line by giving the input file path
as an argument:

```bash
maze-solver input.txt
```

A successfully solved path will be printed out like this:

```
#######E######## ####################
# ### #^<<###### #    #     #     #  
# ### ###^#      #  #    #     #    #
# ### # #^# ###### ##################
# >>> > >^   #       #    #   #   # #
#^ # ##      # ##### #  # # # # # # #
#^ #         #   #   #  # # # # #   #
#^ ######   ###  #  ### # # # # ### #
#^ #    #               #   #   #   #
#^ # ## ########   ## ###########   #
#^   ##          ###                #
#^## #############  ###   ####   ## #
#^<### ##V<<<<<V  #  #  #           #
# ^#   ##V####^V^  #    #      ###  #
# ^# ####V#>V#^V^  #    #####       #
# ^#     V#^>V^V^###           ##   #
# ^##### >>^ V^V^V<#   ##   #   #   #
# ^<<<<< <<< <^<^<^                 #
##################S##################

Total Moves: 74
```

## Maze file format

The maze text file will be constructed into a two-dimensional grid with
fixed width and height. Each character will represent a single cell in
the grid. Every line in the text file must be of the same
length, excluding the last empty line.

The allowed characters in the maze file are:
 - `#`, which will represent a block, or wall (unmovable space)
 - ` ` (single empty space), which will represent a movable space
 - `^`, which is a starting point and
 - `E`, which is an exit point

The program will return an error code and message if the input file format
is invalid.

## Output

On successful execution, the program will print a solution for each start
point in the standard output.

The calculated path is represented with arrow-like characters to display the path.
`^` is up, `V` is down, `<` is left and `>` is right.
To avoid confusion, the starting
point is represented by `S` instead of `^` on the solution output.

## Algorithm

The program uses an algorithm inspired by Trémaux's algorithm. Instead of following already-marked paths (i.e. cells), the algorithm never enters
a cell twice.

This algorithm is not very efficient, but it is a relatively simple one.
