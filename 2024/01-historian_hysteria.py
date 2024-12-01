"""
01-historian_hysteria.py

The solution to the 1st day of Advent of Code 2024
"""

from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / "inputs" / "01.txt"


def first_star() -> list[np.array]:
    """
    Solution to the 1st star problem.

    Returns the parsed coordinates.
    """

    print("+++ FIRST STAR PROBLEM +++")

    coords = [[] for _ in range(2)]

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            coords_line = line.split("   ")

            for i in range(2):
                coords[i].append(int(coords_line[i]))

    coords = [np.array(sorted(l)) for l in coords]

    dist_sum = np.sum(np.abs(coords[0] - coords[1]))
    print(f"Total distance between lists: {dist_sum}")

    return coords


def second_star(coords: list[np.array]) -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    # Count the number occurrences in the 2nd coord
    coord2_occ = {}

    for c in coords[1]:
        if c not in coord2_occ:
            coord2_occ[c] = 0

        coord2_occ[c] += 1

    # Calculate the similarity score
    sim_score = 0

    for c in coords[0]:
        sim_score += c * coord2_occ.get(c, 0)

    print(f"Similarity score: {sim_score}")


if __name__ == "__main__":
    coords = first_star()
    second_star(coords)
