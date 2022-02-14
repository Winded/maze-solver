from imghdr import tests
import setuptools


setuptools.setup(
    name="Maze Solver",
    version="1.0.0",
    author="Antton Hytönen",
    author_email="antton.hytonen@outlook.com",
    description="Solve mazes from text input and render solutions to text output",
    long_description=None,
    url="https://github.com/Winded/maze-solver",
    python_requires='>=3.5',
    packages=['maze_solver'],
    scripts=['bin/maze-solver']
)
