Basic Information

Pynter is a graphical simulation written in Python that demonstrates basic algorithms from sequential game theory.
The simulation consists of a map of fields in space on which spaceships move. When a spaceship passes over a field, it captures it and colors it in its own color.
The game ends when all fields are colored or when the given number of rounds expires.
The goal is to have the most colored fields.

In its turn, a spaceship may choose:

not to move,

to move exactly one field in any direction, or

to begin a continuous movement in any direction that stops when it reaches an abyss or another spaceship.

Using the Application

Run the program from the terminal using:

python .\main.py agents map rounds timeout max_depth


Where:

agents – list of agent names separated by commas (default: all agents are RandomAgent)

map – the map file (default: example_map.txt)

rounds – maximum number of game rounds (default: 5)

timeout – maximum execution time (default: 0; unlimited)

max_depth – maximum search tree depth (default: 5)

Install pygame before running.

The main application window shows the space station map, with a section underneath displaying the current score and the player whose turn it is.

Press SPACE to pause/resume the game.

Press ESC to exit.

Map

The map is a text file containing a matrix representation of fields, abysses, spaceships, and colored fields.
All rows must have equal length.

Name	Symbol	Description
Abyss	0	A field that spaceships cannot move across
Free field	_	A traversable field
Colored field	a, b, c, d	Traversable field that is initially colored
Spaceship	A, B, C, D	A spaceship
System Agents

The system includes the following implemented agents:

RandomAgent – makes random moves

GreedyAgent – chooses the move that yields the highest immediate gain

Students must implement:

MaxNAgent – uses the MaxN algorithm for multiple rational players

MinimaxAgent – uses Minimax for two rational players

MinimaxABAgent – Minimax with alpha–beta pruning for two players

In MaxN, the evaluation function returns a tuple of all agents’ scores.
In the Minimax agents, the evaluation function returns the difference between the agent’s score and the opponent’s score.

User Requirements

Students must extend the Agent class (in agents.py) and override get_chosen_action.
Arguments: state (game state) and max_depth (tree depth limit).
Return value: action represented as:

((src_row, src_col), (dst_row, dst_col))


Two sample agents (RandomAgent, GreedyAgent) are provided.

Example usage:

python .\main.py RandomAgent,RandomAgent example_map.txt 10 0 5


Students are encouraged to test different maps, time limits, and depths.