"""
07-bridge_repair.py

The solution to the 7th day of Advent of Code 2024
"""

from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "07.txt"


def equation_valid(
    val: int,
    terms: list[int],
    running_result: int,
    concat_enabled: bool,
    text_repre: str,
) -> tuple[bool, str | None]:
    """
    Checks whether the equation is valid.
    """

    if running_result == val:
        return True, text_repre
    if running_result > val or len(terms) == 0:
        return False, None

    sum_valid, sum_repre = equation_valid(
        val,
        terms[1:],
        running_result + terms[0],
        concat_enabled,
        text_repre + f" + {terms[0]}",
    )

    mul_valid, mul_repre = equation_valid(
        val,
        terms[1:],
        running_result * terms[0],
        concat_enabled,
        text_repre + f" * {terms[0]}",
    )

    eq_valid = sum_valid or mul_valid
    result_repre = sum_repre if sum_repre is not None else mul_repre

    if concat_enabled:
        concat_valid, concat_repre = equation_valid(
            val,
            terms[1:],
            int(str(running_result) + str(terms[0])),
            concat_enabled,
            text_repre + f" || {terms[0]}",
        )

        eq_valid = eq_valid or concat_valid
        result_repre = result_repre if result_repre is not None else concat_repre

    return eq_valid, result_repre


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    sum_correct = 0

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            val_terms_split = line[:-1].split(": ")
            val = int(val_terms_split[0])
            terms = [int(t) for t in val_terms_split[1].split(" ")]

            is_eq_correct, _ = equation_valid(
                val, terms[1:], terms[0], concat_enabled=False, text_repre=str(terms[0])
            )

            if is_eq_correct:
                sum_correct += val

    print(f"Sum of the values corresponding to correct equations: {sum_correct}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")

    sum_correct = 0
    i = 0

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            val_terms_split = line[:-1].split(": ")
            val = int(val_terms_split[0])
            terms = [int(t) for t in val_terms_split[1].split(" ")]

            is_eq_correct, text_repre = equation_valid(
                val, terms[1:], terms[0], concat_enabled=True, text_repre=str(terms[0])
            )

            if is_eq_correct:
                sum_correct += val

            i += 1

            if i <= 10:
                print(f"{val} = {text_repre}")

    print(f"Sum of the values corresponding to correct equations: {sum_correct}")


if __name__ == "__main__":
    first_star()
    second_star()
