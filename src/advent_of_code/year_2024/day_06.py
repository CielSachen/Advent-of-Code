TITLE = "Guard Gallivant"

type _Coordinates = tuple[int, int]


class NoStartingPositionError(Exception):
    def __init__(self) -> None:
        msg = "The puzzle's input file doesn't contain a starting position"

        super().__init__(msg)

        self.message = msg


def _get_starting_position(map_rows: list[str]) -> _Coordinates:
    guard_key = "^"

    for i, row in enumerate(map_rows):
        if guard_key in row:
            return (row.index(guard_key), i)

    raise NoStartingPositionError


def _get_visited_positions(
    map_rows: list[str], starting_pos: _Coordinates, additional_block_pos: _Coordinates | None = None
) -> set[_Coordinates]:
    max_col_idx = len(map_rows[0])
    max_row_idx = len(map_rows)

    pos_deltas: tuple[_Coordinates, _Coordinates, _Coordinates, _Coordinates] = ((0, -1), (1, 0), (0, 1), (-1, 0))

    visited_positions = {starting_pos}
    directional_visited_positions: set[tuple[_Coordinates, int]] = set()

    curr_pos = starting_pos
    curr_dir = 0

    while True:
        next_col_idx = curr_pos[0] + pos_deltas[curr_dir][0]
        next_row_idx = curr_pos[1] + pos_deltas[curr_dir][1]

        if not 0 <= next_col_idx < max_col_idx or not 0 <= next_row_idx < max_row_idx:
            break

        if map_rows[next_row_idx][next_col_idx] == "#" or (
            additional_block_pos is not None and (next_col_idx, next_row_idx) == additional_block_pos
        ):
            curr_dir = (curr_dir + 1) % len(pos_deltas)
        else:
            curr_pos = (next_col_idx, next_row_idx)

        if additional_block_pos is None and curr_pos not in visited_positions:
            visited_positions.add(curr_pos)

            continue

        if (curr_pos, curr_dir) in directional_visited_positions:
            return set()

        directional_visited_positions.add((curr_pos, curr_dir))

    return visited_positions


def solve_part_1(puzzle_in: str) -> int:
    map_rows = puzzle_in.splitlines()

    return len(_get_visited_positions(map_rows, _get_starting_position(map_rows)))


def solve_part_2(puzzle_in: str) -> int:
    map_rows = puzzle_in.splitlines()
    starting_pos = _get_starting_position(map_rows)

    return sum(
        1
        for pos in _get_visited_positions(map_rows, starting_pos)
        if pos != starting_pos and len(_get_visited_positions(map_rows, starting_pos, additional_block_pos=pos)) == 0
    )
