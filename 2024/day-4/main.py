#!/usr/bin/env python3

import re
from itertools import product


def solve_part_one(input: str) -> None:
    rows = input.splitlines()
    word_count = 0

    for row in rows:
        word_count += len(re.findall(r"(?=(XMAS|SAMX))", row))

    max_rows = len(rows)
    max_columns = len(rows[0])

    for row_number, column_number in product(range(max_rows - 3), range(max_columns)):
        character = rows[row_number][column_number]

        if character == "X" or character == "S":
            if (
                rows[row_number + 1][column_number] == ("M" if character == "X" else "A")
                and rows[row_number + 2][column_number] == ("A" if character == "X" else "M")
                and rows[row_number + 3][column_number] == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_number < max_columns - 3
                and rows[row_number + 1][column_number + 1] == ("M" if character == "X" else "A")
                and rows[row_number + 2][column_number + 2] == ("A" if character == "X" else "M")
                and rows[row_number + 3][column_number + 3] == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_number >= 3
                and rows[row_number + 1][column_number - 1] == ("M" if character == "X" else "A")
                and rows[row_number + 2][column_number - 2] == ("A" if character == "X" else "M")
                and rows[row_number + 3][column_number - 3] == ("S" if character == "X" else "X")
            ):
                word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")


def solve_part_two(input: str) -> None:
    rows = input.splitlines()
    max_rows = len(rows)
    max_columns = len(rows[0])
    word_count = 0

    for row_number, column_number in product(range(max_rows - 2), range(max_columns - 2)):
        character = rows[row_number][column_number]

        if (
            character == "M"
            and rows[row_number][column_number + 2] == "S"
            and rows[row_number + 1][column_number + 1] == "A"
            and rows[row_number + 2][column_number] == "M"
            and rows[row_number + 2][column_number + 2] == "S"
        ):
            word_count += 1

        if (
            character == "S"
            and rows[row_number][column_number + 2] == "M"
            and rows[row_number + 1][column_number + 1] == "A"
            and rows[row_number + 2][column_number] == "S"
            and rows[row_number + 2][column_number + 2] == "M"
        ):
            word_count += 1

        if (
            character == "S"
            and rows[row_number][column_number + 2] == "S"
            and rows[row_number + 1][column_number + 1] == "A"
            and rows[row_number + 2][column_number] == "M"
            and rows[row_number + 2][column_number + 2] == "M"
        ):
            word_count += 1

        if (
            character == "M"
            and rows[row_number][column_number + 2] == "M"
            and rows[row_number + 1][column_number + 1] == "A"
            and rows[row_number + 2][column_number] == "S"
            and rows[row_number + 2][column_number + 2] == "S"
        ):
            word_count += 1

    print(f"Part 2 Puzzle Answer: {word_count}")


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 4 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
