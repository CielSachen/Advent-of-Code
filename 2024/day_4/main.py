#!/usr/bin/env python3

import re
from itertools import product

HORIZONTAL_WORD_PATTERN = r"(?=(XMAS|SAMX))"


def solve_part_one(input: str) -> None:
    word_search_rows = input.splitlines()
    word_count = 0

    for row in word_search_rows:
        word_count += len(re.findall(HORIZONTAL_WORD_PATTERN, row))

    maximum_rows = len(word_search_rows)
    maximum_columns = len(word_search_rows[0])
    HORIZONTAL_PADDING = 3

    for row_number, column_number in product(
        range(maximum_rows - HORIZONTAL_PADDING), range(maximum_columns)
    ):
        character = word_search_rows[row_number][column_number]

        if character == "X" or character == "S":
            if (
                word_search_rows[row_number + 1][column_number]
                == ("M" if character == "X" else "A")
                and word_search_rows[row_number + 2][column_number]
                == ("A" if character == "X" else "M")
                and word_search_rows[row_number + 3][column_number]
                == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_number < maximum_columns - 3
                and word_search_rows[row_number + 1][column_number + 1]
                == ("M" if character == "X" else "A")
                and word_search_rows[row_number + 2][column_number + 2]
                == ("A" if character == "X" else "M")
                and word_search_rows[row_number + 3][column_number + 3]
                == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_number >= 3
                and word_search_rows[row_number + 1][column_number - 1]
                == ("M" if character == "X" else "A")
                and word_search_rows[row_number + 2][column_number - 2]
                == ("A" if character == "X" else "M")
                and word_search_rows[row_number + 3][column_number - 3]
                == ("S" if character == "X" else "X")
            ):
                word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")


def solve_part_two(input: str) -> None:
    word_search_rows = input.splitlines()
    maximum_rows = len(word_search_rows)
    maximum_columns = len(word_search_rows[0])
    PADDING = 2
    word_count = 0

    for row_number, column_number in product(
        range(maximum_rows - PADDING), range(maximum_columns - PADDING)
    ):
        character = word_search_rows[row_number][column_number]

        if (
            character == "M"
            and word_search_rows[row_number][column_number + 2] == "S"
            and word_search_rows[row_number + 1][column_number + 1] == "A"
            and word_search_rows[row_number + 2][column_number] == "M"
            and word_search_rows[row_number + 2][column_number + 2] == "S"
        ):
            word_count += 1

        if (
            character == "S"
            and word_search_rows[row_number][column_number + 2] == "M"
            and word_search_rows[row_number + 1][column_number + 1] == "A"
            and word_search_rows[row_number + 2][column_number] == "S"
            and word_search_rows[row_number + 2][column_number + 2] == "M"
        ):
            word_count += 1

        if (
            character == "S"
            and word_search_rows[row_number][column_number + 2] == "S"
            and word_search_rows[row_number + 1][column_number + 1] == "A"
            and word_search_rows[row_number + 2][column_number] == "M"
            and word_search_rows[row_number + 2][column_number + 2] == "M"
        ):
            word_count += 1

        if (
            character == "M"
            and word_search_rows[row_number][column_number + 2] == "M"
            and word_search_rows[row_number + 1][column_number + 1] == "A"
            and word_search_rows[row_number + 2][column_number] == "S"
            and word_search_rows[row_number + 2][column_number + 2] == "S"
        ):
            word_count += 1

    print(f"Part 2 Puzzle Answer: {word_count}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 4 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
