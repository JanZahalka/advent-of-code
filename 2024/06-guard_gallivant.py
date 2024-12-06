"""
06-guard_gallivant.py

The solution to the 6th day of Advent of Code 2024
"""

from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "06.txt"

TURNS = {
    (1, 0): [0, -1],  # down -> left
    (-1, 0): [0, 1],  # up -> right
    (0, 1): [1, 0],  # right -> down
    (0, -1): [-1, 0],  # left -> up
}


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        floor_map = [list(l[:-1]) for l in f.readlines()]

    r = -1
    c = -1

    # Search for the initial position
    for i, row in enumerate(floor_map):
        for j, char in enumerate(row):
            if char == "^":
                r = i
                c = j

    # Count the number of unique positions visited
    n_unique_visited = 0
    at_the_edge = False
    r_dir = -1
    c_dir = 0

    while not at_the_edge:
        # Check if at the edge, if so, increment one and break
        if (
            r + r_dir < 0
            or r + r_dir == len(floor_map)
            or c + c_dir < 0
            or c + c_dir == len(floor_map[0])
        ):
            n_unique_visited += 1
            break

        # If obstacle ahead, turn right
        if floor_map[r + r_dir][c + c_dir] == "#":
            r_dir, c_dir = TURNS[(r_dir, c_dir)]
        # Otherwise record unique position (if applicable) and go forward
        else:
            if floor_map[r][c] != "X":
                n_unique_visited += 1

            floor_map[r][c] = "X"

            r += r_dir
            c += c_dir

    fm_path = Path(__file__).parent / "inputs" / "06_output.txt"

    with open(fm_path, "w", encoding="utf-8") as f:
        for row in floor_map:
            f.write("".join(row) + "\n")

    print(f"Number of unique visited positions: {n_unique_visited}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")


if __name__ == "__main__":
    first_star()
    second_star()
