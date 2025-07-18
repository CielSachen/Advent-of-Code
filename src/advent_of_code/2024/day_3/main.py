from os import path
from re import findall

INSTRUCTION_PATTERNS = (r"mul\(\d+,\d+\)", r"do\(\)", r"don't\(\)")


def multiply(instruction: str) -> int:
    multiplicand, multiplier = map(int, instruction[4:-1].split(",", maxsplit=1))

    return multiplicand * multiplier


def solve_part_one(puzzle_in: str) -> None:
    mul_instructions: list[str] = findall(INSTRUCTION_PATTERNS[0], puzzle_in)

    results_sum = 0

    for instruction in mul_instructions:
        results_sum += multiply(instruction)

    print(f"Part 1 Puzzle Answer: {results_sum}")


def solve_part_two(puzzle_in: str) -> None:
    instructions: list[str] = findall("|".join(INSTRUCTION_PATTERNS), puzzle_in)
    is_multiplying = True

    results_sum = 0

    for instruction in instructions:
        if instruction == "don't()":
            is_multiplying = False
        elif instruction == "do()":
            is_multiplying = True
        elif is_multiplying:
            results_sum += multiply(instruction)

    print(f"Part 2 Puzzle Answer: {results_sum}")


def main() -> None:
    print("--- Day 3: Mull It Over ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
