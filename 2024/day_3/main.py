#!/usr/bin/env python3

from os import path
from re import findall

INSTRUCTION_PATTERNS = (
    r"mul\([0-9]+,[0-9]+\)",
    r"do\(\)",
    r"don't\(\)",
)


def multiply(instruction: str) -> int:
    numbers = tuple(map(int, instruction[4:-1].split(",", maxsplit=1)))

    return numbers[0] * numbers[1]


def solve_part_one(input: str) -> None:
    multiplication_instructions: list[str] = findall(INSTRUCTION_PATTERNS[0], input)
    results_sum = 0

    for instruction in multiplication_instructions:
        results_sum += multiply(instruction)

    print(f"Part 1 Puzzle Answer: {results_sum}")


def solve_part_two(input: str) -> None:
    instructions: list[str] = findall("|".join(INSTRUCTION_PATTERNS), input)
    should_multiply = True
    results_sum = 0

    for instruction in instructions:
        if instruction == "don't()":
            should_multiply = False
        elif instruction == "do()":
            should_multiply = True
        elif should_multiply:
            results_sum += multiply(instruction)

    print(f"Part 2 Puzzle Answer: {results_sum}")


def main() -> None:
    print("--- Day 3: Mull It Over ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
