"""
02-red_nosed_reports.py

The solution to the 2nd day of Advent of Code 2024
"""

from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "02.txt"


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    n_safe = 0

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            levels = [int(l) for l in line.split(" ")]
            is_increasing = None
            prev_value = None

            for l in levels:
                if prev_value is not None:
                    if l == prev_value:
                        break
                    elif l


                prev_value = l




if __name__ == "__main__":
    first_star()
