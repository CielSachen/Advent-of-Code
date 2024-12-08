#!/usr/bin/env python3

import re


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 4 -----\n")

    with open("input.txt", "r") as input_file:
        rows = input_file.read().splitlines()

    word_count = 0

    for row in rows:
        word_count += len(re.findall(r"(?=(XMAS|SAMX))", row))

    board_height = len(rows)

    for row_number, row in enumerate(rows):
        if row_number >= board_height - 3:
            break

        board_width = len(row)

        for column_number, character in enumerate(row):
            if character == "X":
                if (
                    rows[row_number + 1][column_number] == "M"
                    and rows[row_number + 2][column_number] == "A"
                    and rows[row_number + 3][column_number] == "S"
                ):
                    word_count += 1

                if (
                    column_number < board_width - 3
                    and rows[row_number + 1][column_number + 1] == "M"
                    and rows[row_number + 2][column_number + 2] == "A"
                    and rows[row_number + 3][column_number + 3] == "S"
                ):
                    word_count += 1

                if (
                    column_number >= 3
                    and rows[row_number + 1][column_number - 1] == "M"
                    and rows[row_number + 2][column_number - 2] == "A"
                    and rows[row_number + 3][column_number - 3] == "S"
                ):
                    word_count += 1
            elif character == "S":
                if (
                    rows[row_number + 1][column_number] == "A"
                    and rows[row_number + 2][column_number] == "M"
                    and rows[row_number + 3][column_number] == "X"
                ):
                    word_count += 1

                if (
                    column_number < board_width - 3
                    and rows[row_number + 1][column_number + 1] == "A"
                    and rows[row_number + 2][column_number + 2] == "M"
                    and rows[row_number + 3][column_number + 3] == "X"
                ):
                    word_count += 1

                if (
                    column_number >= 3
                    and rows[row_number + 1][column_number - 1] == "A"
                    and rows[row_number + 2][column_number - 2] == "M"
                    and rows[row_number + 3][column_number - 3] == "X"
                ):
                    word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")

    word_count = 0

    for row_number, row in enumerate(rows):
        if row_number >= board_height - 2:
            break

        board_width = len(row)

        for column_number, character in enumerate(row):
            if column_number < board_width - 2:
                if (
                    character == "M"
                    and row[column_number + 2] == "S"
                    and rows[row_number + 1][column_number + 1] == "A"
                    and rows[row_number + 2][column_number] == "M"
                    and rows[row_number + 2][column_number + 2] == "S"
                ):
                    word_count += 1

                if (
                    character == "S"
                    and row[column_number + 2] == "M"
                    and rows[row_number + 1][column_number + 1] == "A"
                    and rows[row_number + 2][column_number] == "S"
                    and rows[row_number + 2][column_number + 2] == "M"
                ):
                    word_count += 1

                if (
                    character == "S"
                    and row[column_number + 2] == "S"
                    and rows[row_number + 1][column_number + 1] == "A"
                    and rows[row_number + 2][column_number] == "M"
                    and rows[row_number + 2][column_number + 2] == "M"
                ):
                    word_count += 1

                if (
                    character == "M"
                    and row[column_number + 2] == "M"
                    and rows[row_number + 1][column_number + 1] == "A"
                    and rows[row_number + 2][column_number] == "S"
                    and rows[row_number + 2][column_number + 2] == "S"
                ):
                    word_count += 1

    print(f"Part 2 Puzzle Answer: {word_count}")


if __name__ == "__main__":
    main()
