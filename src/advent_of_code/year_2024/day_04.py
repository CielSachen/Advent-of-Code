import itertools
import re

TITLE = "Ceres Search"


def solve_part_1(puzzle_in: str) -> int:
    word_search_rows = puzzle_in.splitlines()
    max_row_idx = len(word_search_rows)
    max_col_idx = len(word_search_rows[0])
    hor_padding_size = 3

    word_cnt = sum(len(re.findall(r"(?=(XMAS|SAMX))", row)) for row in word_search_rows)

    for row_idx, col_idx in itertools.product(range(max_row_idx - hor_padding_size), range(max_col_idx)):
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

    return word_cnt


def solve_part_2(puzzle_in: str) -> int:
    word_search_rows = puzzle_in.splitlines()
    max_row_idx = len(word_search_rows)
    max_col_idx = len(word_search_rows[0])
    padding_size = 2

    word_cnt = 0

    for row_idx, col_idx in itertools.product(range(max_row_idx - padding_size), range(max_col_idx - padding_size)):
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

    return word_cnt
