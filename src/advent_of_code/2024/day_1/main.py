from os import path


def parse_location_ids(puzzle_in: str) -> tuple[list[int], list[int]]:
    left_loc_ids: list[int] = []
    right_loc_ids: list[int] = []

    for id_pair in puzzle_in.splitlines():
        left_id, right_id = map(int, id_pair.split(maxsplit=1))

        left_loc_ids.append(left_id)
        right_loc_ids.append(right_id)

    return left_loc_ids, right_loc_ids


def solve_part_one(puzzle_in: str) -> None:
    left_loc_ids, right_loc_ids = parse_location_ids(puzzle_in)

    left_loc_ids.sort()
    right_loc_ids.sort()

    lists_total_distance = 0

    for left_id, right_id in zip(left_loc_ids, right_loc_ids, strict=False):
        lists_total_distance += abs(left_id - right_id)

    print(f"Part 1 Puzzle Answer: {lists_total_distance}")


def solve_part_two(puzzle_in: str) -> None:
    left_loc_ids, right_loc_ids = parse_location_ids(puzzle_in)

    lists_similarity_score = 0

    for loc_id in left_loc_ids:
        lists_similarity_score += loc_id * right_loc_ids.count(loc_id)

    print(f"Part 2 Puzzle Answer: {lists_similarity_score}")


def main() -> None:
    print("--- Day 1: Historian Hysteria ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
