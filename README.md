# Penne Gameplay Simulation: Documentation
--- 
## **Board**
Class for a square game board.

### Constructor
`def __init__(self, n: int):` Initializes an empty `n`x`n` grid. 
* `n`: An integer indicating the size of the board. 

### Methods
*`add_stone(self, stone: Stone)`* Adds a stone to the board.
* `stone`: A Stone object that represents a player's move.

*`remove_stones(self, stones: List[Stone])`* Removes stones from the board after two stones are flanked. Then, adds one to the player's score. 

* `stones`: A list of Stone objects that represent the stones to be removed.

### Attributes
* `grid`: A 2-dimensional numpy array that represents the board.
---
## **Stone**
Class for a stone on the game board.

### Constructor
`def __init__(self, player: Player, x: int, y: int):`
* `player`: A Player object that represents the player who placed the stone.
* `x`: An integer representing the x-coordinate of the stone on the board.
* `y`: An integer representing the y-coordinate of the stone on the board.
---
## **Player**
Class for a player in the game.

### Constructor
`def __init__(self, id: str, captures: int):`
* `id`: A string representing the player's identifier.
* `captures`: An integer representing the number of opponent's stones the player has captured.

### Methods
*`add_capture(self)`* Increments the number of captures for the player.

### Attributes
* `id`: A string representing the player's identifier (`X` or `O`).
* `captures`: An integer representing the number of opponent's stones the player has captured.
---
## **Game**
Class for the game.

### Constructor
`def __init__(self, moves: List[Tuple[int, int]], board_size: int):`
* `moves`: A list of tuples of integers representing the coordinates `X_i, Y_i` of moves made by the players.
* `board_size`: An integer representing the size of the board.

### Methods
*`scan_array(capture_pattern: str, stone_seq: List[Stone], size: int)`*
Looks in `Board.grid` array for a series of `Stone.player.id`. Returns tuple `is_match: bool, selected_stones: List[Stone]` with `is_match` representing if a match with a sequence of Stone.id objects matches the given pattern. 
* `capture_pattern`: String representing pattern of stone IDs defining a capture
* `stone_seq`: sequence of Stone objects parsed from `Board.grid`, in the direction of one of: `vertical, horizontal, diagonal` 
* `size`: integer defining the number of elements that are considered at once.

*`check(stone_seq: List[Stone], last_player: Player, validate: str)`* Checks `Board.grid` instance for capturing or winning patterns. Returns `str` object containing one of: `'NA'` (game in-progress), `'X'` (Player `X` won the game), `'O'` (Player `O` won the game), `'T'` (tie), `'C'` (a capture was made). 
* `stone_seq`: sequence of Stone objects parsed from `Board.grid`, in the direction of one of: `vertical, horizontal, diagonal`
* `last_player`: A Player object representing the last player who made a move.
* `validate (default='capture')`: A string representing the type of check to perform (`'capture'` or `'win'`).

*`detect(self, board: Board, last_player: Player, validate: str)`*
Checks if a capture or win has been made on the board. Iterates `Board.grid` matrix in vertical, horizontal, and both diagonal directions. After each iteration per direction, `check()` is called and a `str` value is returned. By default, `'NA'` is the default return value. If no other values are returned, the iterations continue. If the iterations complete and `detect()` does not return a value other than `'NA'`, the game continues.

* `board`: A Board object representing the game board.
* `last_player`: A Player object representing the last player who made a move.
* `validate`: A string representing the type of validation to perform ('capture' or 'win').

*`analyze(self, board: Board, last_player: Player)`*
Analyzes the board and returns the outcome of the move. When `validate` parameter is set to `'capture'`, no return value from `detect()` is necessary; a capture will not directly affect the game status. However, the returned value from `detect()` when `validate` is set to `'win'` is returned by the `analyze( )` method. 
* `board`: A Board object representing the game board.
* `last_player`: A Player object representing the last player who made a move.

*`play(self)`*
Simulates the game and returns the outcome of the game. Instantiates `Board` object of size `Game.size`, then iterates through `Game.moves`. In each iteration, a player's stone is placed **(it is assumed the players alternate turns)**, and `Board.grid` is analyzed for captures and/or outcomes. Once an outcome value is returned by `analyze()`, `play()` returns that outcome value.

### Attributes
* `moves`: A list of tuples of integers representing the moves made by the players.
* `board_size`: An integer representing the size of the board.
* `player_x`: A Player object representing the player with identifier 'X'.
* `player_o`: A Player object representing the player with identifier 'O'.

