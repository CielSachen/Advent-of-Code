#!/usr/bin/env python3

from os import path
from typing import Optional

type Coordinates = tuple[int, int]

GUARD_POSITION = "^"
OBSTRUCTION = "#"

POSITION_DELTAS: tuple[Coordinates, Coordinates, Coordinates, Coordinates] = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)


def get_starting_position(map_rows: list[str]) -> Coordinates:
    for row_number, row in enumerate(map_rows):
        if GUARD_POSITION in row:
            return (row.index(GUARD_POSITION), row_number)

    raise Exception(
        "The caret (^) character representing the starting position could not be found."
    )


def get_visited_positions(
    map_rows: list[str],
    starting_position: Coordinates,
    additional_block_position: Optional[Coordinates] = None,
) -> set[Coordinates]:
    current_position = starting_position
    current_direction = 0
    visited_positions = {starting_position}
    directional_visited_positions: set[tuple[Coordinates, int]] = set()

    while True:
        next_position_x = current_position[0] + POSITION_DELTAS[current_direction][0]
        next_position_y = current_position[1] + POSITION_DELTAS[current_direction][1]

        if not 0 <= next_position_x < len(map_rows[0]) or not 0 <= next_position_y < len(map_rows):
            break

        if (
            map_rows[next_position_y][next_position_x] == OBSTRUCTION
            or (next_position_x, next_position_y) == additional_block_position
        ):
            current_direction = (current_direction + 1) % len(POSITION_DELTAS)
        else:
            current_position = (next_position_x, next_position_y)

        if not additional_block_position and current_position not in visited_positions:
            visited_positions.add(current_position)

            continue

        if (current_position, current_direction) in directional_visited_positions:
            return set()

        directional_visited_positions.add((current_position, current_direction))

    return visited_positions


def solve_part_one(input: str) -> None:
    map_rows = input.splitlines()

    print(
        f"Part 1 Puzzle Answer: {len(get_visited_positions(map_rows, get_starting_position(map_rows)))}"
    )


def solve_part_two(input: str) -> None:
    map_rows = input.splitlines()
    starting_position = get_starting_position(map_rows)
    new_block_position_count = 0

    for position in get_visited_positions(map_rows, starting_position):
        if (
            position != starting_position
            and len(
                get_visited_positions(
                    map_rows, starting_position, additional_block_position=position
                )
            )
            == 0
        ):
            new_block_position_count += 1

    print(f"Part 2 Puzzle Answer: {new_block_position_count}")


def main() -> None:
    print("--- Day 6: Guard Gallivant ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        input = input_file.read()

    solve_part_one(input)

    solve_part_two(input)


if __name__ == "__main__":
    main()
