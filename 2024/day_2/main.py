#!/usr/bin/env python3

from os import path


def is_safe(levels: list[int]) -> bool:
    minimum_level_difference = 1
    maximum_level_difference = 3
    level_differences = [levels[index] - levels[index - 1] for index in range(1, len(levels))]

    for first_difference, second_difference in zip(level_differences[:-1], level_differences[1:]):
        if (
            first_difference * second_difference < 0
            or not (minimum_level_difference <= abs(first_difference) <= maximum_level_difference)
            or not (minimum_level_difference <= abs(second_difference) <= maximum_level_difference)
        ):
            return False

    return True


def solve_part_one(input: str) -> None:
    safe_report_count = 0

    for report in input.splitlines():
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            safe_report_count += 1

    print(f"Part 1 Puzzle Answer: {safe_report_count}")


def solve_part_two(input: str) -> None:
    safe_report_count = 0

    for report in input.splitlines():
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            safe_report_count += 1

            continue

        for index in range(len(levels)):
            if is_safe(levels[:index] + levels[index + 1 :]):
                safe_report_count += 1

                break

    print(f"Part 2 Puzzle Answer: {safe_report_count}")


def main() -> None:
    print("--- Day 2: Red-Nosed Reports ---\n")

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
