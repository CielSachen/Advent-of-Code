from collections import defaultdict
from os import path

type CubeSetSizesByColor = dict[str, int]


def parse_game_records(puzzle_in: str) -> list[tuple[int, list[CubeSetSizesByColor]]]:
    game_recs: list[tuple[int, list[CubeSetSizesByColor]]] = []

    for game_rec in puzzle_in.splitlines():
        game_id, cube_sets = game_rec.split(": ", maxsplit=1)

        cube_set_sizes_by_color: list[CubeSetSizesByColor] = []

        for cube_set in cube_sets.split("; "):
            set_size_by_color: CubeSetSizesByColor = defaultdict(int)

            for cube in cube_set.split(", "):
                amt, color = cube.split(maxsplit=1)
                set_size_by_color[color] = int(amt)

            cube_set_sizes_by_color.append(set_size_by_color)

        game_recs.append((int(game_id.replace("Game ", "")), cube_set_sizes_by_color))

    return game_recs


def solve_part_one(puzzle_in: str) -> None:
    max_cube_set_sizes_by_color: CubeSetSizesByColor = {"red": 12, "green": 13, "blue": 14}

    possible_game_ids_sum = 0

    for game_id, cube_set_sizes in parse_game_records(puzzle_in):
        for size in cube_set_sizes:
            if any(size[c] > max_cube_set_sizes_by_color[c] for c in max_cube_set_sizes_by_color):
                break
        else:
            possible_game_ids_sum += game_id

    print(f"Part 1 Puzzle Answer: {possible_game_ids_sum}")


def solve_part_two(puzzle_in: str) -> None:
    min_cube_set_powers_sum = 0

    for _, cube_set_sizes in parse_game_records(puzzle_in):
        min_cube_set_sizes_by_color: CubeSetSizesByColor = {"red": 0, "green": 0, "blue": 0}

        for size in cube_set_sizes:
            min_cube_set_sizes_by_color["red"] = max(min_cube_set_sizes_by_color["red"], size["red"])
            min_cube_set_sizes_by_color["green"] = max(min_cube_set_sizes_by_color["green"], size["green"])
            min_cube_set_sizes_by_color["blue"] = max(min_cube_set_sizes_by_color["blue"], size["blue"])

        min_cube_set_powers_sum += (
            min_cube_set_sizes_by_color["red"]
            * min_cube_set_sizes_by_color["green"]
            * min_cube_set_sizes_by_color["blue"]
        )

    print(f"Part 2 Puzzle Answer: {min_cube_set_powers_sum}")


def main() -> None:
    print("--- Day 2: Cube Conundrum ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
