#!/usr/bin/env python3

import re

FUNCTION_PATTERNS = (r"mul\([0-9]+,[0-9]+\)", r"do\(\)", r"don't\(\)")


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 3 -----\n")

    with open("input.txt", "r") as input_file:
        memory = input_file.read()

    multiplication_functions: list[str] = re.findall(FUNCTION_PATTERNS[0], memory)
    results_sum = 0

    for function in multiplication_functions:
        numbers = list(map(int, function[4:-1].split(",", 1)))

        results_sum += numbers[0] * numbers[1]

    print(f"Part 1 Puzzle Answer: {results_sum}")

    functions = re.findall("|".join(FUNCTION_PATTERNS), memory)
    is_do = True
    results_sum = 0

    for function in functions:
        if function == "don't()":
            is_do = False
        elif function == "do()":
            is_do = True
        elif is_do:
            numbers = list(map(int, function[4:-1].split(",", 1)))

            results_sum += numbers[0] * numbers[1]

    print(f"Part 2 Puzzle Answer: {results_sum}")


if __name__ == "__main__":
    main()
