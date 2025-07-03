from os import path
from re import finditer


def solve_part_one(puzzle_input: str) -> None:
    calibration_values_sum = 0

    for line in puzzle_input.splitlines():
        digits = [int(character) for character in line if character.isdigit()]

        calibration_values_sum += digits[0] * 10 + digits[-1]

    print(f"Part 1 Puzzle Answer: {calibration_values_sum}")


def solve_part_two(puzzle_input: str) -> None:
    integers_by_word = {
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

    for line in puzzle_input.splitlines():
        digits: list[tuple[int, int]] = []

        for word, integer in integers_by_word.items():
            digits.extend((match.start(), integer) for match in finditer(word, line))

        digits.extend((i, int(character)) for i, character in enumerate(line) if character.isdigit())

        digits.sort()

        calibration_values_sum += digits[0][1] * 10 + digits[-1][1]

    print(f"Part 2 Puzzle Answer: {calibration_values_sum}")


def main() -> None:
    print("--- Day 1: Trebuchet?! ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
