# Maze solver

This Python application can solve a maze provided by the input text file.
Python 3 is recommended; the application has not been tested with Python 2.7.

## Installing and testing

TODO

## Usage

To use the program, run it in the command line by giving the input file path
as an argument:

```bash
maze-solver input.txt
```

A successfully solved path will be printed out like this:

```
TODO
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

## Program design

Data structures and the path-finding algorithm are explained in code with line
comments.
