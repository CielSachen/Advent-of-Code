#!/usr/bin/env python3


def is_safe(levels: list[int]) -> bool:
    levels_length = len(levels) - 1
    safe_levels_amount = 0

    for index in range(levels_length):
        if levels[index] < levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            safe_levels_amount += 1

    if safe_levels_amount == levels_length:
        return True

    safe_levels_amount = 0

    for index in range(levels_length):
        if levels[index] > levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            safe_levels_amount += 1

    if safe_levels_amount == levels_length:
        return True

    return False


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 2 -----\n")

    with open("input.txt", "r") as input_file:
        reports = input_file.read().splitlines()

    safe_reports_amount = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_reports_amount += 1

    print(f"Part 1 Puzzle Answer: {safe_reports_amount}")

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


if __name__ == "__main__":
    main()
