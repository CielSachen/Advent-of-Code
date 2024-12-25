#!/usr/bin/env python3

import re

FUNCTION_PATTERNS = (r"mul\([0-9]+,[0-9]+\)", r"do\(\)", r"don't\(\)")


def solve_part_one(input: str) -> None:
    multiplication_functions: list[str] = re.findall(FUNCTION_PATTERNS[0], input)
    results_sum = 0

    for function in multiplication_functions:
        numbers = tuple(map(int, function[4:-1].split(",", 1)))

        results_sum += numbers[0] * numbers[1]

    print(f"Part 1 Puzzle Answer: {results_sum}")


def solve_part_two(input: str) -> None:
    functions = re.findall("|".join(FUNCTION_PATTERNS), input)
    is_do = True
    results_sum = 0

    for function in functions:
        if function == "don't()":
            is_do = False
        elif function == "do()":
            is_do = True
        elif is_do:
            numbers = tuple(map(int, function[4:-1].split(",", 1)))

            results_sum += numbers[0] * numbers[1]

    print(f"Part 2 Puzzle Answer: {results_sum}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 3 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
