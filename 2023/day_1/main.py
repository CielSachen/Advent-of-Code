#!/usr/bin/env python3

from os import path
from re import finditer


def solve_part_one(input: str) -> None:
    calibration_values_sum = 0

    for line in input.splitlines():
        digits = [int(character) for character in line if character.isdigit()]
        calibration_values_sum += digits[0] * 10 + digits[-1]

    print(f"Part 1 Puzzle Answer: {calibration_values_sum}")


def solve_part_two(input: str) -> None:
    word_to_integer = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    calibration_values_sum = 0

    for line in input.splitlines():
        digits: list[tuple[int, int]] = []

        for word in word_to_integer:
            for match in finditer(word, line):
                digits.append((match.start(), word_to_integer[word]))

        for index, character in enumerate(line):
            if character.isdigit():
                digits.append((index, int(character)))

        digits.sort()

        calibration_values_sum += digits[0][1] * 10 + digits[-1][1]

    print(f"Part 2 Puzzle Answer: {calibration_values_sum}")


def main() -> None:
    print("--- Day 1: Trebuchet?! ---\n")

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
