#!/usr/bin/env python3


def is_safe(levels: list[int]) -> bool:
    levels_length = len(levels) - 1
    safe_level_amount = 0

    for index in range(levels_length):
        if levels[index] < levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            safe_level_amount += 1

    if safe_level_amount == levels_length:
        return True

    safe_level_amount = 0

    for index in range(levels_length):
        if levels[index] > levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            safe_level_amount += 1

    if safe_level_amount == levels_length:
        return True

    return False


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 2 -----\n")

    with open("input.txt", "r") as input_file:
        reports = input_file.readlines()

    safe_report_amount = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_report_amount += 1

    print(f"Part 1 Puzzle Answer: {safe_report_amount}")

    safe_report_amount = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_report_amount += 1
        else:
            for index in range(len(levels)):
                tolerated_levels = levels[:index] + levels[index + 1 :]

                if is_safe(tolerated_levels):
                    safe_report_amount += 1

                    break

    print(f"Part 2 Puzzle Answer: {safe_report_amount}")


if __name__ == "__main__":
    main()
