from itertools import product
from os import path
from re import findall


def solve_part_one(puzzle_in: str) -> None:
    word_search_rows = puzzle_in.splitlines()
    max_row_idx = len(word_search_rows)
    max_col_idx = len(word_search_rows[0])
    hor_padding_size = 3

    word_cnt = 0

    for row in word_search_rows:
        word_cnt += len(findall(r"(?=(XMAS|SAMX))", row))

    for row_idx, col_idx in product(range(max_row_idx - hor_padding_size), range(max_col_idx)):
        char = word_search_rows[row_idx][col_idx]

        if char in {"X", "S"}:
            if (
                word_search_rows[row_idx + 1][col_idx] == ("M" if char == "X" else "A")
                and word_search_rows[row_idx + 2][col_idx] == ("A" if char == "X" else "M")
                and word_search_rows[row_idx + 3][col_idx] == ("S" if char == "X" else "X")
            ):
                word_cnt += 1

            if (
                col_idx < max_col_idx - hor_padding_size
                and word_search_rows[row_idx + 1][col_idx + 1] == ("M" if char == "X" else "A")
                and word_search_rows[row_idx + 2][col_idx + 2] == ("A" if char == "X" else "M")
                and word_search_rows[row_idx + 3][col_idx + 3] == ("S" if char == "X" else "X")
            ):
                word_cnt += 1

            if (
                col_idx >= hor_padding_size
                and word_search_rows[row_idx + 1][col_idx - 1] == ("M" if char == "X" else "A")
                and word_search_rows[row_idx + 2][col_idx - 2] == ("A" if char == "X" else "M")
                and word_search_rows[row_idx + 3][col_idx - 3] == ("S" if char == "X" else "X")
            ):
                word_cnt += 1

    print(f"Part 1 Puzzle Answer: {word_cnt}")


def solve_part_two(puzzle_in: str) -> None:
    word_search_rows = puzzle_in.splitlines()
    max_row_idx = len(word_search_rows)
    max_col_idx = len(word_search_rows[0])
    padding_size = 2

    word_cnt = 0

    for row_idx, col_idx in product(range(max_row_idx - padding_size), range(max_col_idx - padding_size)):
        char = word_search_rows[row_idx][col_idx]

        if (
            char == "M"
            and word_search_rows[row_idx][col_idx + 2] == "S"
            and word_search_rows[row_idx + 1][col_idx + 1] == "A"
            and word_search_rows[row_idx + 2][col_idx] == "M"
            and word_search_rows[row_idx + 2][col_idx + 2] == "S"
        ):
            word_cnt += 1

        if (
            char == "S"
            and word_search_rows[row_idx][col_idx + 2] == "M"
            and word_search_rows[row_idx + 1][col_idx + 1] == "A"
            and word_search_rows[row_idx + 2][col_idx] == "S"
            and word_search_rows[row_idx + 2][col_idx + 2] == "M"
        ):
            word_cnt += 1

        if (
            char == "S"
            and word_search_rows[row_idx][col_idx + 2] == "S"
            and word_search_rows[row_idx + 1][col_idx + 1] == "A"
            and word_search_rows[row_idx + 2][col_idx] == "M"
            and word_search_rows[row_idx + 2][col_idx + 2] == "M"
        ):
            word_cnt += 1

        if (
            char == "M"
            and word_search_rows[row_idx][col_idx + 2] == "M"
            and word_search_rows[row_idx + 1][col_idx + 1] == "A"
            and word_search_rows[row_idx + 2][col_idx] == "S"
            and word_search_rows[row_idx + 2][col_idx + 2] == "S"
        ):
            word_cnt += 1

    print(f"Part 2 Puzzle Answer: {word_cnt}")


def main() -> None:
    print("--- Day 4: Ceres Search ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
