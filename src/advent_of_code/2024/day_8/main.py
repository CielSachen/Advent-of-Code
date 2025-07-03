from collections import defaultdict
from itertools import product
from os import path

type Coordinates = tuple[int, int]

type LocationsByAntenna = dict[str, set[Coordinates]]


def get_locations_by_antenna(map_rows: list[str]) -> LocationsByAntenna:
    antenna_to_locations: LocationsByAntenna = defaultdict(set)

    for row_index, column_index in product(range(len(map_rows[0])), range(len(map_rows))):
        character = map_rows[row_index][column_index]

        if character != ".":
            antenna_to_locations[character].add((column_index, row_index))

    return antenna_to_locations


def count_antinodes(
    map_rows: list[str],
    antenna_to_locations: LocationsByAntenna,
    is_ignoring_distance: bool = False,  # noqa: FBT001, FBT002
) -> int:
    max_column_index = len(map_rows[0])
    max_row_index = len(map_rows)

    antinodes: set[Coordinates] = set()

    for antenna in antenna_to_locations:
        locations = antenna_to_locations[antenna]

        if len(locations) == 1:
            continue

        if is_ignoring_distance:
            antinodes = antinodes | locations

        for a, b in product(locations, locations):
            if a == b:
                continue

            (location_x_delta, location_y_delta) = (a[0] - b[0], a[1] - b[1])
            antinode_location: Coordinates = (a[0] + location_x_delta, a[1] + location_y_delta)

            if is_ignoring_distance:
                while True:
                    if (
                        not 0 <= antinode_location[0] < max_column_index
                        or not 0 <= antinode_location[1] < max_row_index
                    ):
                        break

                    antinodes.add(antinode_location)

                    antinode_location = (
                        antinode_location[0] + location_x_delta,
                        antinode_location[1] + location_y_delta,
                    )
            elif (
                0 <= antinode_location[0] < max_column_index
                and 0 <= antinode_location[1] < max_row_index
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
            count_antinodes(map_rows, get_locations_by_antenna(map_rows), is_ignoring_distance=True)
        }"
    )


def main() -> None:
    print("--- Day 8: Resonant Collinearity ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
