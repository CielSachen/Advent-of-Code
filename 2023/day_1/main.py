#!/usr/bin/env python3

import re


def solve_part_one(input: str) -> None:
    calibration_document_lines: list[str] = input.splitlines()
    calibration_values_sum = 0

    for line in calibration_document_lines:
        digits = [character for character in line if character.isdigit()]

        if len(digits) > 0:
            calibration_values_sum += int(digits[0] + digits[-1])

    print(f"Part 1 Puzzle Answer: {calibration_values_sum}")


def solve_part_two(input: str) -> None:
    calibration_document_lines: list[str] = input.splitlines()
    word_to_integer = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    calibration_values_sum = 0

    for line in calibration_document_lines:
        digits: list[tuple[int, str]] = []

        for word in word_to_integer:
            for match in re.finditer(word, line):
                digits.append((match.start(), word_to_integer[match.group(0)]))

        for index, character in enumerate(line):
            if character.isdigit():
                digits.append((index, character))

        digits.sort()

        calibration_values_sum += int(digits[0][1] + digits[-1][1])

    print(f"Part 2 Puzzle Answer: {calibration_values_sum}")


def main() -> None:
    print("----- ADVENT OF CODE : 2023 : DAY 1 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
