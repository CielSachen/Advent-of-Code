import itertools

TITLE = "Historian Hysteria"


def _parse_location_ids(puzzle_in: str) -> tuple[list[int], list[int]]:
    left_loc_ids: list[int] = []
    right_loc_ids: list[int] = []

    for left_id, right_id in itertools.batched(puzzle_in.split(), 2, strict=True):
        left_loc_ids.append(int(left_id))
        right_loc_ids.append(int(right_id))

    return left_loc_ids, right_loc_ids


def solve_part_1(puzzle_in: str) -> int:
    left_loc_ids, right_loc_ids = _parse_location_ids(puzzle_in)

    left_loc_ids.sort()
    right_loc_ids.sort()

    return sum(abs(left_id - right_id) for left_id, right_id in zip(left_loc_ids, right_loc_ids, strict=False))


def solve_part_2(puzzle_in: str) -> int:
    left_loc_ids, right_loc_ids = _parse_location_ids(puzzle_in)

    return sum(left_id * right_loc_ids.count(left_id) for left_id in left_loc_ids)
