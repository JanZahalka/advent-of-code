"""
06-guard_gallivant.py

The solution to the 6th day of Advent of Code 2024
"""

import copy
from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "06.txt"

TURNS = {
    (1, 0): [0, -1],  # down -> left
    (-1, 0): [0, 1],  # up -> right
    (0, 1): [1, 0],  # right -> down
    (0, -1): [-1, 0],  # left -> up
}


def load_input_find_init_pos() -> tuple[list[str], int, int]:
    """
    Loads the input and finds the row & col index of the starting position.
    """
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

    return floor_map, r, c


def first_star() -> list[list[tuple[int, int], tuple[int, int]]]:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    # Load the input and initial position
    floor_map, r, c = load_input_find_init_pos()

    # Count the number of unique positions visited
    n_unique_visited = 0
    visited = []
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

            visited.append([(r, c), (r_dir, c_dir)])
            floor_map[r][c] = "X"

            r += r_dir
            c += c_dir

    fm_path = Path(__file__).parent / "inputs" / "06_output.txt"

    with open(fm_path, "w", encoding="utf-8") as f:
        for row in floor_map:
            f.write("".join(row) + "\n")

    print(f"Number of unique visited positions: {n_unique_visited}")

    return visited


def second_star(visited_orig: list[list[tuple[int], tuple[int]]]) -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    # Load the input and initial position
    floor_map, r0, c0 = load_input_find_init_pos()

    valid_obstacle_positions = set()
    n_valid_obstacles = 0

    # Go over the locations visited in the normal path sans the initial position
    for p in range(1, len(visited_orig)):
        # The guard starts at the previous position in the given direction
        prev_pos = visited_orig[p - 1]

        r = prev_pos[0][0]
        c = prev_pos[0][1]
        r_dir = prev_pos[1][0]
        c_dir = prev_pos[1][1]
        """
        r = r0
        c = c0
        r_dir = -1
        c_dir = 0
        """
        # print(f"Start at {r, c}, direction ({r_dir}, {c_dir})")

        # The obstacle is placed at the position
        pos = visited_orig[p]
        r_obst = pos[0][0]
        c_obst = pos[0][1]

        # print(f"Obstacle at {r_obst, c_obst}")
        floor_map_obst = copy.deepcopy(floor_map)
        floor_map_obst[r_obst][c_obst] = "O"

        # Flag the starting point
        if r_dir == 0 and c_dir == 1:
            # Right
            start_marker = ">"
        elif r_dir == 0 and c_dir == -1:
            # Left
            start_marker = "<"
        elif r_dir == 1 and c_dir == 0:
            # Down
            start_marker = "v"
        elif r_dir == -1 and c_dir == 0:
            # Up
            start_marker = "^"
        else:
            raise ValueError("Wrong direction coordinates.")

        floor_map_obst[r][c] = start_marker

        # Unflag the orig starting point
        floor_map_obst[r0][c0] = "."

        # Traverse and check for loops
        at_the_edge = False
        looped = False
        visited_obst = []

        while not at_the_edge:
            # Break at the edge
            if (
                r + r_dir < 0
                or r + r_dir == len(floor_map_obst)
                or c + c_dir < 0
                or c + c_dir == len(floor_map_obst[0])
            ):
                # print(f"Leaving at {r}, {c}, direction ({r_dir}, {c_dir})")
                break

            # Detect loop if the position has been already visited
            if [(r, c), (r_dir, c_dir)] in visited_obst:
                looped = True
                break

            visited_obst.append([(r, c), (r_dir, c_dir)])

            # If obstacle ahead, turn right
            if floor_map_obst[r + r_dir][c + c_dir] in ["#", "O"]:
                r_dir, c_dir = TURNS[(r_dir, c_dir)]
            # Otherwise record unique position (if applicable) and go forward
            else:
                if floor_map_obst[r][c] == ".":
                    floor_map_obst[r][c] = "X"
                r += r_dir
                c += c_dir

        if looped:
            n_valid_obstacles += 1

        if (p + 1) % 100 == 0:
            print(f"{p+1} candidates processed.")
            """
            print(f"Candidate {p}: {looped}")

            fm_path = Path(__file__).parent / "inputs" / f"06_output_2_{p}.txt"

            with open(fm_path, "w", encoding="utf-8") as f:
                for row in floor_map_obst:
                    f.write("".join(row) + "\n")
            """

    print(f"Number of obstacles that can cause a guard loop: {n_valid_obstacles}")


if __name__ == "__main__":
    visited = first_star()
    second_star(visited)
