from collections import defaultdict
from itertools import product
from os import path

type Coordinates = tuple[int, int]

type LocationsByAntenna = dict[str, set[Coordinates]]


def get_locations_by_antenna(map_rows: list[str]) -> LocationsByAntenna:
    antenna_to_locations: LocationsByAntenna = defaultdict(set)

    for row_number, column_number in product(range(len(map_rows[0])), range(len(map_rows))):
        character = map_rows[row_number][column_number]

        if character != ".":
            antenna_to_locations[character].add((column_number, row_number))

    return antenna_to_locations


def count_antinodes(
    map_rows: list[str],
    antenna_to_locations: LocationsByAntenna,
    should_ignore_distance: bool = False,  # noqa: FBT001, FBT002
) -> int:
    maximum_column_number = len(map_rows[0])
    maximum_row_number = len(map_rows)

    antinodes: set[Coordinates] = set()

    for antenna in antenna_to_locations:
        locations = antenna_to_locations[antenna]

        if len(locations) == 1:
            continue

        if should_ignore_distance:
            antinodes = antinodes | locations

        for first_location, second_location in product(locations, locations):
            if first_location == second_location:
                continue

            (location_delta_x, location_delta_y) = (
                first_location[0] - second_location[0],
                first_location[1] - second_location[1],
            )
            antinode_location: Coordinates = (
                first_location[0] + location_delta_x,
                first_location[1] + location_delta_y,
            )

            if should_ignore_distance:
                while True:
                    if (
                        not 0 <= antinode_location[0] < maximum_column_number
                        or not 0 <= antinode_location[1] < maximum_row_number
                    ):
                        break

                    antinodes.add(antinode_location)

                    antinode_location = (
                        antinode_location[0] + location_delta_x,
                        antinode_location[1] + location_delta_y,
                    )
            elif (
                0 <= antinode_location[0] < maximum_column_number
                and 0 <= antinode_location[1] < maximum_row_number
                and antinode_location not in locations
            ):
                antinodes.add(antinode_location)

    return len(antinodes)


def solve_part_one(puzzle_input: str) -> None:
    map_rows = puzzle_input.splitlines()

    print(f"Part 1 Puzzle Answer: {count_antinodes(map_rows, get_locations_by_antenna(map_rows))}")


def solve_part_two(puzzle_input: str) -> None:
    map_rows = puzzle_input.splitlines()

    print(
        f"Part 2 Puzzle Answer: {
            count_antinodes(
                map_rows, get_locations_by_antenna(map_rows), should_ignore_distance=True
            )
        }"
    )


def main() -> None:
    print("--- Day 8: Resonant Collinearity ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
