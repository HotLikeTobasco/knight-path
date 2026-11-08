"""Shortest knight routes on an otherwise empty chessboard."""
import argparse
from collections import deque


def square(value):
    value = value.lower()
    if len(value) != 2 or value[0] not in "abcdefgh" or value[1] not in "12345678":
        raise argparse.ArgumentTypeError("use a square from a1 to h8")
    return value


def route(start, end):
    start, end = square(start), square(end)
    queue = deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        if path[-1] == end:
            return path
        x, y = ord(path[-1][0]) - 97, int(path[-1][1]) - 1
        for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = chr(97 + nx) + str(ny + 1)
                if target not in seen:
                    seen.add(target)
                    queue.append(path + [target])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=square)
    parser.add_argument("end", type=square)
    args = parser.parse_args()
    path = route(args.start, args.end)
    print(" -> ".join(path))
    print(f"{len(path) - 1} moves")


if __name__ == "__main__":
    main()
