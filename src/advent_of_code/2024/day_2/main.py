from itertools import pairwise
from os import path


def is_safe(levels: list[int]) -> bool:
    min_level_difference = 1
    max_level_difference = 3
    level_differences = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

    for a, b in pairwise(level_differences):
        if (
            a * b < 0
            or not (min_level_difference <= abs(a) <= max_level_difference)
            or not (min_level_difference <= abs(b) <= max_level_difference)
        ):
            return False

    return True


def solve_part_one(puzzle_input: str) -> None:
    safe_report_count = 0

    for report in puzzle_input.splitlines():
        if is_safe([int(level) for level in report.split()]):
            safe_report_count += 1

    print(f"Part 1 Puzzle Answer: {safe_report_count}")


def solve_part_two(puzzle_input: str) -> None:
    safe_report_count = 0

    for report in puzzle_input.splitlines():
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            safe_report_count += 1

            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                safe_report_count += 1

                break

    print(f"Part 2 Puzzle Answer: {safe_report_count}")


def main() -> None:
    print("--- Day 2: Red-Nosed Reports ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
