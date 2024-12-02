"""
02-red_nosed_reports.py

The solution to the 2nd day of Advent of Code 2024
"""

import copy
from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "02.txt"


def _process_level_list(levels: list[int]) -> tuple[bool, int | None]:
    """
    Processes a single level list and returns whether it is safe or not and
    the index of the offender (or None if no failure was detected).
    """
    is_increasing = None
    is_safe = True
    offender_index = None

    for i in range(1, len(levels)):
        # Vals cannot be equal
        if levels[i] == levels[i - 1]:
            is_safe = False
            offender_index = i
            break

        if is_increasing is None:
            is_increasing = levels[i] > levels[i - 1]

        trend_upheld = (is_increasing and levels[i] > levels[i - 1]) or (
            not is_increasing and levels[i] < levels[i - 1]
        )
        difference = abs(levels[i] - levels[i - 1])

        if not trend_upheld or difference > 3:
            is_safe = False
            offender_index = i
            break

    return is_safe, offender_index


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    n_safe = 0

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            levels = [int(l) for l in line.split(" ")]
            is_safe, _ = _process_level_list(levels)

            if is_safe:
                n_safe += 1

    print(f"Number of safe level reports: {n_safe}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    n_safe = 0

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            levels = [int(l) for l in line.split(" ")]
            levels_orig = copy.deepcopy(levels)

            # Check the list
            is_safe, offender_index = _process_level_list(levels)

            # If it's not safe, try the following four cases:
            # 1) Removing the entry at the offending index
            # 2) Removing the entry at offending index - 1
            # 3) Removing the first entry (which may set the wrong trend)
            # 4) Removing the final entry (which may break an otherwise kept trend)
            if not is_safe:
                # Offending index
                del levels[offender_index]
                is_safe_off_idx, _ = _process_level_list(levels)

                # Offending index - 1
                levels = copy.deepcopy(levels_orig)
                del levels[offender_index - 1]
                is_safe_off_idx_min1, _ = _process_level_list(levels)

                # Offending index - 1
                levels = copy.deepcopy(levels_orig)
                del levels[0]
                is_safe_first, _ = _process_level_list(levels)

                # Offending index - 1
                levels = copy.deepcopy(levels_orig)
                del levels[-1]
                is_safe_last, _ = _process_level_list(levels)

                # If any of those work, then it's safe
                is_safe = (
                    is_safe_off_idx
                    or is_safe_off_idx_min1
                    or is_safe_first
                    or is_safe_last
                )

            if is_safe:
                n_safe += 1

    print(f"Number of safe level reports with Problem Dampener: {n_safe}")


if __name__ == "__main__":
    first_star()
    second_star()
