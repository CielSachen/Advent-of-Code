import re

TITLE = "Mull It Over"


def _multiply(instruction: str) -> int:
    multiplicand, multiplier = map(int, instruction[4:-1].split(",", maxsplit=1))

    return multiplicand * multiplier


_INSTRUCTION_PATTERNS = (r"mul\(\d+,\d+\)", r"do\(\)", r"don't\(\)")


def solve_part_1(puzzle_in: str) -> int:
    return sum(_multiply(instruction) for instruction in re.findall(_INSTRUCTION_PATTERNS[0], puzzle_in))


def solve_part_2(puzzle_in: str) -> int:
    instructions: list[str] = re.findall("|".join(_INSTRUCTION_PATTERNS), puzzle_in)
    is_multiplying = True

    results_sum = 0

    for instruction in instructions:
        if instruction == "don't()":
            is_multiplying = False
        elif instruction == "do()":
            is_multiplying = True
        elif is_multiplying:
            results_sum += _multiply(instruction)

    return results_sum
