from collections import defaultdict
from itertools import product
from os import path

type Coordinates = tuple[int, int]

type LocationsByAntenna = dict[str, set[Coordinates]]


def get_locations_by_antenna(map_rows: list[str]) -> LocationsByAntenna:
    locs_by_antenna: LocationsByAntenna = defaultdict(set)

    for row_idx, col_idx in product(range(len(map_rows[0])), range(len(map_rows))):
        char = map_rows[row_idx][col_idx]

        if char != ".":
            locs_by_antenna[char].add((col_idx, row_idx))

    return locs_by_antenna


def count_antinodes(
    map_rows: list[str],
    locs_by_antenna: LocationsByAntenna,
    ignore_distance: bool = False,  # noqa: FBT001, FBT002
) -> int:
    max_col_idx = len(map_rows[0])
    max_row_idx = len(map_rows)

    antinodes: set[Coordinates] = set()

    for antenna in locs_by_antenna:
        locs = locs_by_antenna[antenna]

        if len(locs) == 1:
            continue

        if ignore_distance:
            antinodes = antinodes | locs

        for a, b in product(locs, locs):
            if a == b:
                continue

            (loc_x_delta, loc_y_delta) = (a[0] - b[0], a[1] - b[1])
            antinode_loc: Coordinates = (a[0] + loc_x_delta, a[1] + loc_y_delta)

            if ignore_distance:
                while True:
                    if not 0 <= antinode_loc[0] < max_col_idx or not 0 <= antinode_loc[1] < max_row_idx:
                        break

                    antinodes.add(antinode_loc)

                    antinode_loc = (antinode_loc[0] + loc_x_delta, antinode_loc[1] + loc_y_delta)
            elif 0 <= antinode_loc[0] < max_col_idx and 0 <= antinode_loc[1] < max_row_idx and antinode_loc not in locs:
                antinodes.add(antinode_loc)

    return len(antinodes)


def solve_part_one(puzzle_in: str) -> None:
    map_rows = puzzle_in.splitlines()

    print(f"Part 1 Puzzle Answer: {count_antinodes(map_rows, get_locations_by_antenna(map_rows))}")


def solve_part_two(puzzle_in: str) -> None:
    map_rows = puzzle_in.splitlines()

    print(
        f"Part 2 Puzzle Answer: {count_antinodes(map_rows, get_locations_by_antenna(map_rows), ignore_distance=True)}"
    )


def main() -> None:
    print("--- Day 8: Resonant Collinearity ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
