"""
04-ceres_search.py

The solution to the 4th day of Advent of Code 2024
"""

from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "04.txt"

PATTERN_FIRST_STAR = "XMAS"

PATTERNS_SECOND_STAR = ["SAM", "MAS"]


def _first_star_pattern_match(
    text: str, c: int, i: int, j: int, i_dir: int, j_dir: int
) -> int:
    """
    Recursive pattern matching. Returns 0 if the pattern failed to match, 1 if it did match.
    """
    # Failure stop condition: i or j index out of bounds of the text 2D array
    if i < 0 or i >= len(text) or j < 0 or j >= len(text[i]):
        return 0

    # If the i-jth letter matches the c-th pattern char, either succeed (if pattern matched)
    # or continue the search at the next position
    if text[i][j] == PATTERN_FIRST_STAR[c]:
        if c == len(PATTERN_FIRST_STAR) - 1:
            return 1
        else:
            return _first_star_pattern_match(
                text, c + 1, i + i_dir, j + j_dir, i_dir, j_dir
            )
    # If there is no match, return False, the pattern wasn't matched
    else:
        return 0


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        text = [l[:-1] for l in f.readlines()]

    n_patterns = 0

    for i, line in enumerate(text):
        for j, char in enumerate(line):
            # Search patterns if X
            if char == PATTERN_FIRST_STAR[0]:
                n_patterns += _first_star_pattern_match(text, 1, i + 1, j, 1, 0)
                n_patterns += _first_star_pattern_match(text, 1, i - 1, j, -1, 0)
                n_patterns += _first_star_pattern_match(text, 1, i, j + 1, 0, 1)
                n_patterns += _first_star_pattern_match(text, 1, i, j - 1, 0, -1)
                n_patterns += _first_star_pattern_match(text, 1, i + 1, j + 1, 1, 1)
                n_patterns += _first_star_pattern_match(text, 1, i - 1, j - 1, -1, -1)
                n_patterns += _first_star_pattern_match(text, 1, i + 1, j - 1, 1, -1)
                n_patterns += _first_star_pattern_match(text, 1, i - 1, j + 1, -1, 1)

    print(f"Number of {PATTERN_FIRST_STAR} patterns in the text: {n_patterns}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        text = [l[:-1] for l in f.readlines()]

    n_patterns = 0

    for i, line in enumerate(text):
        for j, char in enumerate(line):
            # Continue if the letter doesn't match or too close to the edge
            if i > len(text) - 3 or j > len(line) - 3:
                continue

            # Set the requirement for the bottom right chars...
            if char == "M":
                bottom_right = "S"
            elif char == "S":
                bottom_right = "M"
            # ... or continue if no match
            else:
                continue

            # Set the requirement for the bottom left char...
            if line[j + 2] == "M":
                bottom_left = "S"
            elif line[j + 2] == "S":
                bottom_left = "M"
            else:
                continue

            # Perform the final pattern check
            if (
                text[i + 1][j + 1] == "A"
                and text[i + 2][j] == bottom_left
                and text[i + 2][j + 2] == bottom_right
            ):
                n_patterns += 1

    print(f"Number of X-MAS patterns in the text: {n_patterns}")


if __name__ == "__main__":
    first_star()
    second_star()
