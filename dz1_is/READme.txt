Basic Information

Lost in Spyce is a graphical simulation written in Python that demonstrates the operation of basic search algorithms.
The simulation consists of a map of fields in space on which spaceships move using predefined search strategies. Some fields contain parking spots that spaceships need to reach.
The goal of the simulation is to bring all spaceships to their designated parking spots.

Spaceships can move in any direction and will continue traveling across traversable fields until they hit an obstacle field or another spaceship, where they stop.
For this purpose, several algorithms must be implemented to solve the problem.

Using the Application

The program is run from the terminal using the following command:

python .\main.py algorithm map timeout


Where:

.\main.py – path to the main Python file

algorithm – the name of the search algorithm to use (default: ExampleAlgorithm)

map – the name of the map file (default: example_map.txt)

timeout – maximum execution time (default: 0; unlimited)

Before running the program, the pygame package must be installed.

After starting, the main application window will appear, displaying the map of the space station and spaceship movement.

Press SPACE to start or pause the solution animation.

Press ENTER to display the final solution.

Press ESC to exit the application.

Map

The map is a text file containing a matrix representation of fields, obstacles, spaceships, and parking spots.
All rows must contain the same number of characters.

Example map:

Name	Symbol	Description
Empty field	_	Field on which spaceships can move
Obstacle	O	Field that stops the spaceship
Spaceship	S	A spaceship
Parking spot	G	Goal
System Algorithms

There are several types of spaceships, each with its own search strategy:

Blue – Depth-First Search (DFS), neighbor order: north, east, south, west

Red – Breadth-First Search (BFS), same neighbor order

Black – Branch and Bound search, movement cost = number of crossed fields, tie-breaking neighbor order: N/E/S/W

White – A* search using Manhattan distance, same movement cost and tie-breaking rules

User Requirements

Students must implement search strategies by extending the Algorithm class (found in algorithms.py) and overriding its get_path method.
The parameter state represents the system state, and the return value is the final list of actions that lead to the goal.

Each action is a tuple of the spaceship’s starting and ending positions:

((src_row, src_col), (dst_row, dst_col))


An example class ExampleAlgorithm is provided.

Example usage:

python .\main.py ExampleAlgorithm example_map.txt 5


Note: new maps, algorithms, and heuristics may be introduced during the project defense.

Implementation must be done in Python using standard libraries and data structures.