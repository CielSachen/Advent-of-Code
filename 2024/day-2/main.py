#!/usr/bin/env python3


def is_safe(levels: list[int]) -> bool:
    levels_length = len(levels) - 1
    safe_level_count = 0

    for index in range(levels_length):
        if levels[index] < levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            safe_level_count += 1

    if safe_level_count == levels_length:
        return True

    new_safe_level_count = 0

    for index in range(levels_length):
        if levels[index] > levels[index + 1] and abs(levels[index] - levels[index + 1]) <= 3:
            new_safe_level_count += 1

    if new_safe_level_count == levels_length:
        return True

    return False


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 2 -----\n")

    input_file = open("input.txt", "r")
    reports = input_file.readlines()

    input_file.close()

    safe_report_count = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_report_count += 1

    print(f"Part 1 Puzzle Answer: {safe_report_count}")

    new_safe_report_count = 0

    for report in reports:
        levels = list(map(int, report.split()))

        if is_safe(levels):
            new_safe_report_count += 1
        else:
            for index in range(len(levels)):
                tolerated_levels = levels[:index] + levels[index + 1 :]

                if is_safe(tolerated_levels):
                    new_safe_report_count += 1

                    break

    print(f"Part 2 Puzzle Answer: {new_safe_report_count}")


if __name__ == "__main__":
    main()
