from itertools import product
from os import path
from re import findall


def solve_part_one(puzzle_input: str) -> None:
    word_search_rows = puzzle_input.splitlines()
    max_row_index = len(word_search_rows)
    max_column_index = len(word_search_rows[0])
    horizontal_padding_size = 3

    word_count = 0

    for row in word_search_rows:
        word_count += len(findall(r"(?=(XMAS|SAMX))", row))

    for row_index, column_index in product(range(max_row_index - horizontal_padding_size), range(max_column_index)):
        character = word_search_rows[row_index][column_index]

        if character in {"X", "S"}:
            if (
                word_search_rows[row_index + 1][column_index] == ("M" if character == "X" else "A")
                and word_search_rows[row_index + 2][column_index] == ("A" if character == "X" else "M")
                and word_search_rows[row_index + 3][column_index] == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_index < max_column_index - horizontal_padding_size
                and word_search_rows[row_index + 1][column_index + 1] == ("M" if character == "X" else "A")
                and word_search_rows[row_index + 2][column_index + 2] == ("A" if character == "X" else "M")
                and word_search_rows[row_index + 3][column_index + 3] == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_index >= horizontal_padding_size
                and word_search_rows[row_index + 1][column_index - 1] == ("M" if character == "X" else "A")
                and word_search_rows[row_index + 2][column_index - 2] == ("A" if character == "X" else "M")
                and word_search_rows[row_index + 3][column_index - 3] == ("S" if character == "X" else "X")
            ):
                word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")


def solve_part_two(puzzle_input: str) -> None:
    word_search_rows = puzzle_input.splitlines()
    max_row_index = len(word_search_rows)
    max_column_index = len(word_search_rows[0])
    padding_size = 2

    word_count = 0

    for row_index, column_index in product(range(max_row_index - padding_size), range(max_column_index - padding_size)):
        character = word_search_rows[row_index][column_index]

        if (
            character == "M"
            and word_search_rows[row_index][column_index + 2] == "S"
            and word_search_rows[row_index + 1][column_index + 1] == "A"
            and word_search_rows[row_index + 2][column_index] == "M"
            and word_search_rows[row_index + 2][column_index + 2] == "S"
        ):
            word_count += 1

        if (
            character == "S"
            and word_search_rows[row_index][column_index + 2] == "M"
            and word_search_rows[row_index + 1][column_index + 1] == "A"
            and word_search_rows[row_index + 2][column_index] == "S"
            and word_search_rows[row_index + 2][column_index + 2] == "M"
        ):
            word_count += 1

        if (
            character == "S"
            and word_search_rows[row_index][column_index + 2] == "S"
            and word_search_rows[row_index + 1][column_index + 1] == "A"
            and word_search_rows[row_index + 2][column_index] == "M"
            and word_search_rows[row_index + 2][column_index + 2] == "M"
        ):
            word_count += 1

        if (
            character == "M"
            and word_search_rows[row_index][column_index + 2] == "M"
            and word_search_rows[row_index + 1][column_index + 1] == "A"
            and word_search_rows[row_index + 2][column_index] == "S"
            and word_search_rows[row_index + 2][column_index + 2] == "S"
        ):
            word_count += 1

    print(f"Part 2 Puzzle Answer: {word_count}")


def main() -> None:
    print("--- Day 4: Ceres Search ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
