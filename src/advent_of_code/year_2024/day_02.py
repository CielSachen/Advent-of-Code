import itertools

TITLE = "Red-Nosed Reports"


def _is_safe(levels: list[int]) -> bool:
    min_lvl_diff = 1
    max_lvl_diff = 3

    for a, b in itertools.pairwise(levels[i] - levels[i - 1] for i in range(1, len(levels))):
        if a * b < 0 or not (min_lvl_diff <= abs(a) <= max_lvl_diff) or not (min_lvl_diff <= abs(b) <= max_lvl_diff):
            return False

    return True


def solve_part_1(puzzle_in: str) -> int:
    return sum(1 for report in puzzle_in.splitlines() if _is_safe(list(map(int, report.split()))))


def solve_part_2(puzzle_in: str) -> int:
    num_safe_reports = 0

    for report in puzzle_in.splitlines():
        levels = list(map(int, report.split()))

        if _is_safe(levels):
            num_safe_reports += 1

            continue

        for i in range(len(levels)):
            if _is_safe(levels[:i] + levels[i + 1 :]):
                num_safe_reports += 1

                break

    return num_safe_reports
