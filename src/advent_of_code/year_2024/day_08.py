import collections
import itertools

TITLE = "Resonant Collinearity"

type _Coordinates = tuple[int, int]
type _LocationsByAntenna = dict[str, set[_Coordinates]]


def _get_locations_by_antenna(map_rows: list[str]) -> _LocationsByAntenna:
    locs_by_antenna: _LocationsByAntenna = collections.defaultdict(set)

    for row_idx, col_idx in itertools.product(range(len(map_rows[0])), range(len(map_rows))):
        if (char := map_rows[row_idx][col_idx]) != ".":
            locs_by_antenna[char].add((col_idx, row_idx))

    return locs_by_antenna


def _count_antinodes(
    map_rows: list[str], locs_by_antenna: _LocationsByAntenna, *, ignore_distance: bool = False
) -> int:
    max_col_idx = len(map_rows[0])
    max_row_idx = len(map_rows)

    antinodes: set[_Coordinates] = set()

    for antenna in locs_by_antenna:
        locs = locs_by_antenna[antenna]

        if len(locs) == 1:
            continue

        if ignore_distance:
            antinodes |= locs

        for a, b in itertools.product(locs, locs):
            if a == b:
                continue

            (loc_dx, loc_dy) = (a[0] - b[0], a[1] - b[1])

            antinode_loc: _Coordinates = (a[0] + loc_dx, a[1] + loc_dy)

            if ignore_distance:
                while 0 <= antinode_loc[0] < max_col_idx and 0 <= antinode_loc[1] < max_row_idx:
                    antinodes.add(antinode_loc)

                    antinode_loc = (antinode_loc[0] + loc_dx, antinode_loc[1] + loc_dy)
            elif antinode_loc not in locs and 0 <= antinode_loc[0] < max_col_idx and 0 <= antinode_loc[1] < max_row_idx:
                antinodes.add(antinode_loc)

    return len(antinodes)


def solve_part_1(puzzle_in: str) -> int:
    map_rows = puzzle_in.splitlines()

    return _count_antinodes(map_rows, _get_locations_by_antenna(map_rows))


def solve_part_2(puzzle_in: str) -> int:
    map_rows = puzzle_in.splitlines()

    return _count_antinodes(map_rows, _get_locations_by_antenna(map_rows), ignore_distance=True)
