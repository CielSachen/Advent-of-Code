from itertools import product
from os import path
from re import findall


def solve_part_one(puzzle_input: str) -> None:
    word_search_rows = puzzle_input.splitlines()
    maximum_row_number = len(word_search_rows)
    maximum_column_number = len(word_search_rows[0])
    horizontal_padding_size = 3

    word_count = 0

    for row in word_search_rows:
        word_count += len(findall(r"(?=(XMAS|SAMX))", row))

    for row_number, column_number in product(
        range(maximum_row_number - horizontal_padding_size), range(maximum_column_number)
    ):
        character = word_search_rows[row_number][column_number]

        if character in {"X", "S"}:
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
                column_number < maximum_column_number - horizontal_padding_size
                and word_search_rows[row_number + 1][column_number + 1]
                == ("M" if character == "X" else "A")
                and word_search_rows[row_number + 2][column_number + 2]
                == ("A" if character == "X" else "M")
                and word_search_rows[row_number + 3][column_number + 3]
                == ("S" if character == "X" else "X")
            ):
                word_count += 1

            if (
                column_number >= horizontal_padding_size
                and word_search_rows[row_number + 1][column_number - 1]
                == ("M" if character == "X" else "A")
                and word_search_rows[row_number + 2][column_number - 2]
                == ("A" if character == "X" else "M")
                and word_search_rows[row_number + 3][column_number - 3]
                == ("S" if character == "X" else "X")
            ):
                word_count += 1

    print(f"Part 1 Puzzle Answer: {word_count}")


def solve_part_two(puzzle_input: str) -> None:
    word_search_rows = puzzle_input.splitlines()
    maximum_row_number = len(word_search_rows)
    maximum_column_number = len(word_search_rows[0])
    padding_size = 2

    word_count = 0

    for row_number, column_number in product(
        range(maximum_row_number - padding_size), range(maximum_column_number - padding_size)
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
    print("--- Day 4: Ceres Search ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
