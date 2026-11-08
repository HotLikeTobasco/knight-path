# Knight Path

Two squares. One knight. The shortest way across the board.

A tiny Python tool that finds a shortest knight route on an empty 8×8 chessboard using breadth-first search. No installs or API keys needed.

## Run

Requires Python 3.9 or newer. Download or clone this repository, then run:

```sh
python3 knight.py a1 h8
```

```text
a1 -> b3 -> c5 -> d7 -> f8 -> g6 -> h8
6 moves
```

Squares are case-insensitive. Invalid squares are rejected. Starting and ending on the same square takes zero moves.

## How it works

Each square is a node; each legal knight jump is an edge. Breadth-first search visits squares in increasing distance, so the first route to the destination uses the fewest moves. When several routes tie, the tool returns one of them.

This is an empty-board visualisation aid: it does not account for other pieces, checks, or full-game legality.
