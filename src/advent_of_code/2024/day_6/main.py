from os import path

type Coordinates = tuple[int, int]

GUARD_KEY = "^"
OBSTRUCTION_KEY = "#"


class NoStartingPositionError(Exception):
    def __init__(self) -> None:
        super().__init__("The puzzle input doesn't contain a starting position.")


def get_starting_position(map_rows: list[str]) -> Coordinates:
    for row_index, row in enumerate(map_rows):
        if GUARD_KEY in row:
            return (row.index(GUARD_KEY), row_index)

    raise NoStartingPositionError


POSITION_DELTAS: tuple[Coordinates, Coordinates, Coordinates, Coordinates] = ((0, -1), (1, 0), (0, 1), (-1, 0))
POSITION_DELTA_COUNT = len(POSITION_DELTAS)


def get_visited_positions(
    map_rows: list[str], starting_position: Coordinates, additional_block_position: Coordinates | None = None
) -> set[Coordinates]:
    max_column_index = len(map_rows[0])
    max_row_index = len(map_rows)

    current_position = starting_position
    current_direction = 0

    visited_positions = {starting_position}
    directional_visited_positions: set[tuple[Coordinates, int]] = set()

    while True:
        next_column_index = current_position[0] + POSITION_DELTAS[current_direction][0]
        next_row_index = current_position[1] + POSITION_DELTAS[current_direction][1]

        if not 0 <= next_column_index < max_column_index or not 0 <= next_row_index < max_row_index:
            break

        if map_rows[next_row_index][next_column_index] == OBSTRUCTION_KEY or (
            additional_block_position is not None and (next_column_index, next_row_index) == additional_block_position
        ):
            current_direction = (current_direction + 1) % POSITION_DELTA_COUNT
        else:
            current_position = (next_column_index, next_row_index)

        if additional_block_position is None and current_position not in visited_positions:
            visited_positions.add(current_position)

            continue

        if (current_position, current_direction) in directional_visited_positions:
            return set()

        directional_visited_positions.add((current_position, current_direction))

    return visited_positions


def solve_part_one(puzzle_input: str) -> None:
    map_rows = puzzle_input.splitlines()

    print(f"Part 1 Puzzle Answer: {len(get_visited_positions(map_rows, get_starting_position(map_rows)))}")


def solve_part_two(puzzle_input: str) -> None:
    map_rows = puzzle_input.splitlines()
    starting_position = get_starting_position(map_rows)

    new_block_position_count = 0

    for position in get_visited_positions(map_rows, starting_position):
        if (
            position != starting_position
            and len(get_visited_positions(map_rows, starting_position, additional_block_position=position)) == 0
        ):
            new_block_position_count += 1

    print(f"Part 2 Puzzle Answer: {new_block_position_count}")


def main() -> None:
    print("--- Day 6: Guard Gallivant ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
