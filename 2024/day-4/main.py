#!/usr/bin/env python3

import re


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 4 -----\n")

    with open("input.txt", "r") as input_file:
        rows = input_file.readlines()

    word_count = 0

    for row in rows:
        word_count += len(re.findall(r"(?=(XMAS|SAMX))", row))

    rows_length = len(rows)

    for rows_index, row in enumerate(rows):
        if rows_index >= rows_length - 3:
            break

        row_length = len(row)

        for row_index, character in enumerate(row):
            if character == "X":
                if (
                    rows[rows_index + 1][row_index] == "M"
                    and rows[rows_index + 2][row_index] == "A"
                    and rows[rows_index + 3][row_index] == "S"
                ):
                    word_count += 1

                if (
                    row_index < row_length - 3
                    and rows[rows_index + 1][row_index + 1] == "M"
                    and rows[rows_index + 2][row_index + 2] == "A"
                    and rows[rows_index + 3][row_index + 3] == "S"
                ):
                    word_count += 1

                if (
                    row_index >= 3
                    and rows[rows_index + 1][row_index - 1] == "M"
                    and rows[rows_index + 2][row_index - 2] == "A"
                    and rows[rows_index + 3][row_index - 3] == "S"
                ):
                    word_count += 1
            elif character == "S":
                if (
                    rows[rows_index + 1][row_index] == "A"
                    and rows[rows_index + 2][row_index] == "M"
                    and rows[rows_index + 3][row_index] == "X"
                ):
                    word_count += 1

                if (
                    row_index < row_length - 3
                    and rows[rows_index + 1][row_index + 1] == "A"
                    and rows[rows_index + 2][row_index + 2] == "M"
                    and rows[rows_index + 3][row_index + 3] == "X"
                ):
                    word_count += 1

                if (
                    row_index >= 3
                    and rows[rows_index + 1][row_index - 1] == "A"
                    and rows[rows_index + 2][row_index - 2] == "M"
                    and rows[rows_index + 3][row_index - 3] == "X"
                ):
                    word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")

    word_count = 0

    for rows_index, row in enumerate(rows):
        if rows_index >= rows_length - 2:
            break

        row_length = len(row)

        for row_index, character in enumerate(row):
            if row_index < row_length - 2:
                if (
                    character == "M"
                    and row[row_index + 2] == "S"
                    and rows[rows_index + 1][row_index + 1] == "A"
                    and rows[rows_index + 2][row_index] == "M"
                    and rows[rows_index + 2][row_index + 2] == "S"
                ):
                    word_count += 1

                if (
                    character == "S"
                    and row[row_index + 2] == "M"
                    and rows[rows_index + 1][row_index + 1] == "A"
                    and rows[rows_index + 2][row_index] == "S"
                    and rows[rows_index + 2][row_index + 2] == "M"
                ):
                    word_count += 1

                if (
                    character == "S"
                    and row[row_index + 2] == "S"
                    and rows[rows_index + 1][row_index + 1] == "A"
                    and rows[rows_index + 2][row_index] == "M"
                    and rows[rows_index + 2][row_index + 2] == "M"
                ):
                    word_count += 1

                if (
                    character == "M"
                    and row[row_index + 2] == "M"
                    and rows[rows_index + 1][row_index + 1] == "A"
                    and rows[rows_index + 2][row_index] == "S"
                    and rows[rows_index + 2][row_index + 2] == "S"
                ):
                    word_count += 1

    print(f"Part 2 Puzzle Answer: {word_count}")


if __name__ == "__main__":
    main()
