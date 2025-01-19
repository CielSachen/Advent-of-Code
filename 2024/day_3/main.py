#!/usr/bin/env python3

import re

INSTRUCTION_PATTERN = {"mul()": r"mul\([0-9]+,[0-9]+\)", "do()": r"do\(\)", "don't()": r"don't\(\)"}


def multiply(function: str) -> int:
    numbers = list(map(int, function[4:-1].split(",", maxsplit=1)))

    return numbers[0] * numbers[1]


def solve_part_one(input: str) -> None:
    multiplication_functions: list[str] = re.findall(INSTRUCTION_PATTERN["mul()"], input)
    results_sum = 0

    for function in multiplication_functions:
        results_sum += multiply(function)

    print(f"Part 1 Puzzle Answer: {results_sum}")


def solve_part_two(input: str) -> None:
    functions: list[str] = re.findall("|".join(INSTRUCTION_PATTERN.values()), input)
    should_multiply = True
    results_sum = 0

    for function in functions:
        if function == "don't()":
            should_multiply = False
        elif function == "do()":
            should_multiply = True
        elif should_multiply:
            results_sum += multiply(function)

    print(f"Part 2 Puzzle Answer: {results_sum}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 3 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
