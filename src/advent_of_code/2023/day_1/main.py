from os import path
from re import finditer


def solve_part_one(puzzle_in: str) -> None:
    calibration_vals_sum = 0

    for line in puzzle_in.splitlines():
        digits = [int(c) for c in line if c.isdigit()]

        calibration_vals_sum += digits[0] * 10 + digits[-1]

    print(f"Part 1 Puzzle Answer: {calibration_vals_sum}")


def solve_part_two(puzzle_in: str) -> None:
    digits_by_word = {
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

    calibration_vals_sum = 0

    for line in puzzle_in.splitlines():
        digits: list[tuple[int, int]] = []

        for word, digit in digits_by_word.items():
            digits.extend((m.start(), digit) for m in finditer(word, line))

        digits.extend((i, int(c)) for i, c in enumerate(line) if c.isdigit())

        digits.sort()

        calibration_vals_sum += digits[0][1] * 10 + digits[-1][1]

    print(f"Part 2 Puzzle Answer: {calibration_vals_sum}")


def main() -> None:
    print("--- Day 1: Trebuchet?! ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
