#!/usr/bin/env python3

from collections import defaultdict
from itertools import product

type OrderedPair = tuple[int, int]


def get_antenna_locations_map(map_rows: list[str]) -> dict[str, set[OrderedPair]]:
    maximum_columns = len(map_rows[0])
    maximum_rows = len(map_rows)
    antenna_to_locations: defaultdict[str, set[OrderedPair]] = defaultdict(set)

    for row_number, column_number in product(range(maximum_columns), range(maximum_rows)):
        character = map_rows[row_number][column_number]

        if character != ".":
            antenna_to_locations[character].add((column_number, row_number))

    return antenna_to_locations


def count_antinodes(
    map_rows: list[str],
    antenna_to_locations: dict[str, set[OrderedPair]],
    should_ignore_distance: bool = False,
) -> int:
    maximum_columns = len(map_rows[0])
    maximum_rows = len(map_rows)
    antinodes: set[OrderedPair] = set()

    for antenna in antenna_to_locations:
        locations = antenna_to_locations[antenna]

        if len(locations) == 1:
            continue

        if should_ignore_distance:
            antinodes = antinodes.union(locations)

        for location, other_location in product(locations, locations):
            if location == other_location:
                continue

            (location_delta_x, location_delta_y) = (
                location[0] - other_location[0],
                location[1] - other_location[1],
            )
            antinode_location: OrderedPair = (
                location[0] + location_delta_x,
                location[1] + location_delta_y,
            )

            if should_ignore_distance:
                while True:
                    if not (0 <= antinode_location[0] < maximum_columns) or not (
                        0 <= antinode_location[1] < maximum_rows
                    ):
                        break

                    antinodes.add(antinode_location)

                    antinode_location = (
                        antinode_location[0] + location_delta_x,
                        antinode_location[1] + location_delta_y,
                    )
            elif (
                0 <= antinode_location[0] < maximum_columns
                and 0 <= antinode_location[1] < maximum_rows
                and antinode_location not in locations
            ):
                antinodes.add(antinode_location)

    return len(antinodes)


def solve_part_one(input: str) -> None:
    map_rows = input.splitlines()

    print(f"Part 1 Puzzle Answer: {count_antinodes(map_rows, get_antenna_locations_map(map_rows))}")


def solve_part_two(input: str) -> None:
    map_rows = input.splitlines()

    print(
        f"Part 2 Puzzle Answer: {
            count_antinodes(
                map_rows, get_antenna_locations_map(map_rows), should_ignore_distance=True
            )
        }"
    )


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 8 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
