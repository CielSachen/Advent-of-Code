import itertools
import math
from collections.abc import Generator

TITLE = "Cube Conundrum"

type _GameRecord = tuple[int, int, int]


def _parse_game_records(puzzle_in: str) -> Generator[_GameRecord]:
    for raw_game_rec in puzzle_in.splitlines():
        red_cube_amount = 0
        green_cube_amount = 0
        blue_cube_amount = 0

        for amount, color in itertools.batched(raw_game_rec.split()[2:], 2, strict=True):
            match color.rstrip(",;"):
                case "red":
                    red_cube_amount = max(red_cube_amount, int(amount))
                case "green":
                    green_cube_amount = max(green_cube_amount, int(amount))
                case "blue":
                    blue_cube_amount = max(blue_cube_amount, int(amount))
                case _:
                    pass

        yield (red_cube_amount, green_cube_amount, blue_cube_amount)


def solve_part_1(puzzle_in: str) -> int:
    max_game_rec: _GameRecord = (12, 13, 14)

    possible_game_ids_sum = 0

    for i, game_rec in enumerate(_parse_game_records(puzzle_in)):
        if all(cube_cnt <= max_game_rec[i] for i, cube_cnt in enumerate(game_rec)):
            possible_game_ids_sum += i + 1

    return possible_game_ids_sum


def solve_part_2(puzzle_in: str) -> int:
    return sum(math.prod(game_rec) for game_rec in _parse_game_records(puzzle_in))
