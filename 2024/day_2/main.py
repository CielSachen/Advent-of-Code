#!/usr/bin/env python3

MINIMUM_LEVEL_DIFFERENCE = 1
MAXIMUM_LEVEL_DIFFERENCE = 3


def is_safe(levels: list[int]) -> bool:
    level_differences = [levels[index] - levels[index - 1] for index in range(1, len(levels))]

    for first_difference, second_difference in zip(level_differences[:-1], level_differences[1:]):
        if (
            first_difference * second_difference < 0
            or not (MINIMUM_LEVEL_DIFFERENCE <= abs(first_difference) <= MAXIMUM_LEVEL_DIFFERENCE)
            or not (MINIMUM_LEVEL_DIFFERENCE <= abs(second_difference) <= MAXIMUM_LEVEL_DIFFERENCE)
        ):
            return False

    return True


def solve_part_one(input: str) -> None:
    reports = input.splitlines()
    safe_reports_count = 0

    for report in reports:
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            safe_reports_count += 1

    print(f"Part 1 Puzzle Answer: {safe_reports_count}")


def solve_part_two(input: str) -> None:
    reports = input.splitlines()
    safe_reports_count = 0

    for report in reports:
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            safe_reports_count += 1

            continue

        for index in range(len(levels)):
            if is_safe(levels[:index] + levels[index + 1 :]):
                safe_reports_count += 1

                break

    print(f"Part 2 Puzzle Answer: {safe_reports_count}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 2 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
