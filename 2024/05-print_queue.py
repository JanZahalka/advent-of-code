"""
05-ceres_search.py

The solution to the 5th day of Advent of Code 2024
"""

from pathlib import Path

INPUT_PATH = Path(__file__).parent / "inputs" / "05.txt"


def _rules(input_text: list[str]) -> tuple[dict, int]:
    """
    Extracts the rules dict and the index of the first line of the update specs
    """
    rules = {}
    i = 0

    for line in input_text:
        if line == "":
            i += 1
            break

        pages = line.split("|")

        # Process the pages
        for p in range(2):
            if pages[p] not in rules:
                rules[pages[p]] = {}
                rules[pages[p]]["prev"] = []
                rules[pages[p]]["next"] = []

        rules[pages[0]]["next"].append(pages[1])
        rules[pages[1]]["prev"].append(pages[0])

        i += 1

    return rules, i


def _update_correctness(updates_list: list[str], rules: dict) -> list[bool]:
    """
    For a given list of updates, returns a list of bool values of the
    same length that records whether the updates are correct or not
    according to the rules
    """

    update_correctness = []

    for update_raw in updates_list:
        update_pages = update_raw.split(",")
        update_correct = True

        for up, update_page in enumerate(update_pages):
            # No previous pages may be listed as next
            for p in range(up):
                if update_pages[p] in rules[update_page]["next"]:
                    update_correct = False

            # No following pages may be listed as previous
            for n in range(up + 1, len(update_pages)):
                if update_pages[n] in rules[update_page]["prev"]:
                    update_correct = False

        update_correctness.append(update_correct)

    return update_correctness


def first_star() -> None:
    """
    Solution to the 1st star problem.
    """

    print("+++ FIRST STAR PROBLEM +++")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_text = [l[:-1] for l in f.readlines()]

    # Process the rules
    rules, i = _rules(input_text)

    # Sum the middle page from the correct updates
    update_correctness = _update_correctness(input_text[i:], rules)

    middle_page_sum = 0
    for update_raw, update_correct in zip(input_text[i:], update_correctness):
        update_pages = update_raw.split(",")

        if update_correct:
            middle_page_sum += int(update_pages[len(update_pages) // 2])

    print(f"Sum of middle pages of the correct updates: {middle_page_sum}")


def second_star() -> None:
    """
    Solution to the 2nd star problem.
    """

    print("+++ SECOND STAR PROBLEM +++")
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        input_text = [l[:-1] for l in f.readlines()]

    # Process the rules
    rules, i = _rules(input_text)

    update_correctness = _update_correctness(input_text[i:], rules)

    # Reorder and sum
    corrected_mid_page_sum = 0

    for update_raw, update_correct in zip(input_text[i:], update_correctness):
        if update_correct:
            continue

        update_pages = update_raw.split(",")

        # Count the number of antecedents
        n_antecedents = {}

        for update_page in update_pages:
            n_antecedents[update_page] = 0

            for update_page2 in update_pages:
                if update_page2 in rules[update_page]["prev"]:
                    n_antecedents[update_page] += 1

        # Sort the dict by key
        n_antecedents = {
            k: v for k, v in sorted(n_antecedents.items(), key=lambda item: item[1])
        }
        reordered_pages = list(n_antecedents.keys())
        corrected_mid_page_sum += int(reordered_pages[len(reordered_pages) // 2])

    print(
        f"Sum of middle pages of the corrected updates only: {corrected_mid_page_sum}"
    )


if __name__ == "__main__":
    first_star()
    second_star()
