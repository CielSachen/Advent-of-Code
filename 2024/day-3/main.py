#!/usr/bin/env python3

import re

MULTIPLICATION_FUNCTION_REGEX = r"mul\([0-9]+,[0-9]+\)"


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 3 -----\n")

    input_file = open("input.txt", "r")
    memory = input_file.read()

    input_file.close()

    multiplication_functions: list[str] = re.findall(MULTIPLICATION_FUNCTION_REGEX, memory)
    results_sum = 0

    for function in multiplication_functions:
        numbers = list(map(int, function[4:-1].split(",")))

        results_sum += numbers[0] * numbers[1]

    print(f"Part 1 Puzzle Answer: {results_sum}")

    functions = re.findall(rf"{MULTIPLICATION_FUNCTION_REGEX}|do\(\)|don't\(\)", memory)
    is_do = True
    new_results_sum = 0

    for function in functions:
        if function == "don't()":
            is_do = False
        elif function == "do()":
            is_do = True
        elif is_do:
            numbers = list(map(int, function[4:-1].split(",")))

            new_results_sum += numbers[0] * numbers[1]

    print(f"Part 2 Puzzle Answer: {new_results_sum}")


if __name__ == "__main__":
    main()
