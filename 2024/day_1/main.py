from os import path


def parse_location_ids(puzzle_input: str) -> tuple[list[int], list[int]]:
    left_location_ids: list[int] = []
    right_location_ids: list[int] = []

    for id_pair in puzzle_input.splitlines():
        ids = tuple(map(int, id_pair.split(maxsplit=1)))

        left_location_ids.append(ids[0])
        right_location_ids.append(ids[1])

    return left_location_ids, right_location_ids


def solve_part_one(puzzle_input: str) -> None:
    left_location_ids, right_location_ids = parse_location_ids(puzzle_input)

    left_location_ids.sort()
    right_location_ids.sort()

    lists_total_distance = 0

    for left_id, right_id in zip(left_location_ids, right_location_ids, strict=False):
        lists_total_distance += abs(left_id - right_id)

    print(f"Part 1 Puzzle Answer: {lists_total_distance}")


def solve_part_two(puzzle_input: str) -> None:
    left_location_ids, right_location_ids = parse_location_ids(puzzle_input)

    lists_similarity_score = 0

    for location_id in left_location_ids:
        lists_similarity_score += location_id * right_location_ids.count(location_id)

    print(f"Part 2 Puzzle Answer: {lists_similarity_score}")


def main() -> None:
    print("--- Day 1: Historian Hysteria ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
