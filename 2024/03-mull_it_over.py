"""
03-mull_it_over.py

The solution to the 3rd day of Advent of Code 2024
"""

from pathlib import Path
import re

INPUT_PATH = Path(__file__).parent / "inputs" / "03.txt"


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    input_data = INPUT_PATH.read_text()

    muls = re.findall("mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)", input_data)
    muls = [m.replace("mul(", "") for m in muls]
    muls = [m.replace(")", "") for m in muls]
    muls = [[int(o) for o in m.split(",")] for m in muls]

    sum_muls = 0

    for mul in muls:
        sum_muls += mul[0] * mul[1]

    print(f"Sum of valid multiples: {sum_muls}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    input_data = INPUT_PATH.read_text()

    instr = re.findall(
        "mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)|do\\(\\)|don't\\(\\)", input_data
    )

    sum_muls = 0
    enabled = True

    for i in instr:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        elif enabled:
            i = i.replace("mul(", "")
            i = i.replace(")", "")
            i = [int(o) for o in i.split(",")]

            sum_muls += i[0] * i[1]

    print(f"Sum of valid and enabled multiples: {sum_muls}")


if __name__ == "__main__":
    first_star()
    second_star()
