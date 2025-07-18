from os import path

type Coordinates = tuple[int, int]

GUARD_KEY = "^"
OBSTRUCTION_KEY = "#"


class NoStartingPositionError(Exception):
    def __init__(self) -> None:
        super().__init__("The puzzle input doesn’t contain a starting position.")


def get_starting_position(map_rows: list[str]) -> Coordinates:
    for i, row in enumerate(map_rows):
        if GUARD_KEY in row:
            return (row.index(GUARD_KEY), i)

    raise NoStartingPositionError


POSITION_DELTAS: tuple[Coordinates, Coordinates, Coordinates, Coordinates] = ((0, -1), (1, 0), (0, 1), (-1, 0))
POSITION_DELTA_COUNT = len(POSITION_DELTAS)


def get_visited_positions(
    map_rows: list[str], starting_position: Coordinates, additional_block_position: Coordinates | None = None
) -> set[Coordinates]:
    max_col_idx = len(map_rows[0])
    max_row_idx = len(map_rows)

    curr_pos = starting_position
    curr_dir = 0

    visited_positions = {starting_position}
    directional_visited_positions: set[tuple[Coordinates, int]] = set()

    while True:
        next_col_idx = curr_pos[0] + POSITION_DELTAS[curr_dir][0]
        next_row_idx = curr_pos[1] + POSITION_DELTAS[curr_dir][1]

        if not 0 <= next_col_idx < max_col_idx or not 0 <= next_row_idx < max_row_idx:
            break

        if map_rows[next_row_idx][next_col_idx] == OBSTRUCTION_KEY or (
            additional_block_position is not None and (next_col_idx, next_row_idx) == additional_block_position
        ):
            curr_dir = (curr_dir + 1) % POSITION_DELTA_COUNT
        else:
            curr_pos = (next_col_idx, next_row_idx)

        if additional_block_position is None and curr_pos not in visited_positions:
            visited_positions.add(curr_pos)

            continue

        if (curr_pos, curr_dir) in directional_visited_positions:
            return set()

        directional_visited_positions.add((curr_pos, curr_dir))

    return visited_positions


def solve_part_one(puzzle_in: str) -> None:
    map_rows = puzzle_in.splitlines()

    print(f"Part 1 Puzzle Answer: {len(get_visited_positions(map_rows, get_starting_position(map_rows)))}")


def solve_part_two(puzzle_in: str) -> None:
    map_rows = puzzle_in.splitlines()
    starting_pos = get_starting_position(map_rows)

    new_block_pos_cnt = 0

    for pos in get_visited_positions(map_rows, starting_pos):
        if (
            pos != starting_pos
            and len(get_visited_positions(map_rows, starting_pos, additional_block_position=pos)) == 0
        ):
            new_block_pos_cnt += 1

    print(f"Part 2 Puzzle Answer: {new_block_pos_cnt}")


def main() -> None:
    print("--- Day 6: Guard Gallivant ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
