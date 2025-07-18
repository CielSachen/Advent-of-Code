from itertools import pairwise
from os import path


def is_safe(levels: list[int]) -> bool:
    min_lvl_diff = 1
    max_lvl_diff = 3
    lvl_diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

    for a, b in pairwise(lvl_diffs):
        if a * b < 0 or not (min_lvl_diff <= abs(a) <= max_lvl_diff) or not (min_lvl_diff <= abs(b) <= max_lvl_diff):
            return False

    return True


def solve_part_one(puzzle_in: str) -> None:
    safe_report_cnt = 0

    for report in puzzle_in.splitlines():
        if is_safe(list(map(int, report.split()))):
            safe_report_cnt += 1

    print(f"Part 1 Puzzle Answer: {safe_report_cnt}")


def solve_part_two(puzzle_in: str) -> None:
    safe_report_cnt = 0

    for report in puzzle_in.splitlines():
        levels = list(map(int, report.split()))

        if is_safe(levels):
            safe_report_cnt += 1

            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                safe_report_cnt += 1

                break

    print(f"Part 2 Puzzle Answer: {safe_report_cnt}")


def main() -> None:
    print("--- Day 2: Red-Nosed Reports ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
