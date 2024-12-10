#!/usr/bin/env python3


def is_safe(levels: list[int]) -> bool:
    level_differences = [levels[index] - levels[index - 1] for index in range(1, len(levels))]

    for first_difference, second_difference in zip(level_differences[:-1], level_differences[1:]):
        if (
            first_difference * second_difference < 0
            or not (1 <= abs(first_difference) <= 3)
            or not (1 <= abs(second_difference) <= 3)
        ):
            return False

    return True


def solve_part_one(input: str) -> None:
    reports = input.splitlines()
    safe_reports_amount = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_reports_amount += 1

    print(f"Part 1 Puzzle Answer: {safe_reports_amount}")


def solve_part_two(input: str) -> None:
    reports = input.splitlines()
    safe_reports_amount = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_reports_amount += 1
        else:
            for index in range(len(levels)):
                if is_safe(levels[:index] + levels[index + 1 :]):
                    safe_reports_amount += 1

                    break

    print(f"Part 2 Puzzle Answer: {safe_reports_amount}")


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 2 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
