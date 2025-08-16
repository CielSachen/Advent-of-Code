import re

TITLE = "Trebuchet?!"


def solve_part_1(puzzle_in: str) -> int:
    calibration_vals_sum = 0

    for line in puzzle_in.splitlines():
        digits = [char for char in line if char.isdigit()]

        calibration_vals_sum += int(digits[0] + digits[-1])

    return calibration_vals_sum


def solve_part_2(puzzle_in: str) -> int:
    digit_to_word = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    calibration_vals_sum = 0

    for line in puzzle_in.splitlines():
        digits: list[tuple[int, str]] = []

        for digit, word in digit_to_word.items():
            digits.extend((match.start(), digit) for match in re.finditer(word, line))

        digits.extend((i, char) for i, char in enumerate(line) if char.isdigit())

        digits.sort()

        calibration_vals_sum += int(digits[0][1] + digits[-1][1])

    return calibration_vals_sum
