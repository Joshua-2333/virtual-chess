# Virtual Chess 

A simple interactive chessboard simulator built in Python.

This project is a text-based chessboard that allows you to move, place, remove, reset, clear, and fill pieces on an 8×8 board using terminal commands.

It does **not** enforce chess rules — it acts as a board state simulator for learning Python data structures.

---

## Features

* Interactive command-line chessboard
* Dictionary-based board representation
* Move pieces between squares
* Add or remove pieces manually
* Reset board to starting positions
* Clear the board completely
* Fill the board with any piece
* Custom ASCII board rendering

---

## Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* String formatting
  
---

## Commands

### Move a piece

```bash
move e2 e4
```

Moves a piece from `e2` to `e4`.

---

### Remove a piece

```bash
remove e4
```

Removes the piece at `e4`.

---

### Set a piece

```bash
set d5 wQ
```

Places a white queen at `d5`.

Piece format:

* `wP` = White Pawn
* `wN` = White Knight
* `wB` = White Bishop
* `wR` = White Rook
* `wQ` = White Queen
* `wK` = White King
* `bP` = Black Pawn
* `bN` = Black Knight
* `bB` = Black Bishop
* `bR` = Black Rook
* `bQ` = Black Queen
* `bK` = Black King

---

### Reset the board

```bash
reset
```

Restores the default chess setup.

---

### Clear the board

```bash
clear
```

Removes all pieces.

---

### Fill the board

```bash
fill wP
```

Fills all 64 squares with white pawns.

---

### Quit

```bash
quit
```

Exits the simulator.

---

## Example Gameplay

```text
> move e2 e4
> move e7 e5
> set d4 wQ
> remove e5
> reset
> quit
```

---

## Future Improvements

* Validate legal chess moves
* Add turn tracking
* Piece capturing
* Check/checkmate detection
* Save/load board states
* Undo moves
* Multiplayer support

---

## Learning Goals

This project was built to practice:

* Modeling real-world objects with Python dictionaries
* Using command handlers instead of long if/elif chains
* Building interactive terminal applications
* Managing program state

---

