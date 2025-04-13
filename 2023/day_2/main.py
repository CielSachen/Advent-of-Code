#!/usr/bin/env python3

from collections import defaultdict
from os import path

type CubeSetSizesByColor = dict[str, int]


def parse_game_records(
    input: str,
) -> list[tuple[int, list[CubeSetSizesByColor]]]:
    game_records: list[tuple[int, list[CubeSetSizesByColor]]] = []

    for game_record in input.splitlines():
        id, cube_sets = game_record.split(": ", maxsplit=1)
        cube_set_sizes: list[CubeSetSizesByColor] = []

        for set in cube_sets.split("; "):
            set_size: CubeSetSizesByColor = defaultdict(int)

            for cube in set.split(", "):
                amount, color = cube.split(maxsplit=1)
                set_size[color] = int(amount)

            cube_set_sizes.append(set_size)

        game_records.append((int(id.replace("Game ", "")), cube_set_sizes))

    return game_records


def solve_part_one(input: str) -> None:
    color_to_maximum_cube_set_size: CubeSetSizesByColor = {"red": 12, "green": 13, "blue": 14}
    possible_game_ids_sum = 0

    for id, cube_set_sizes in parse_game_records(input):
        is_possible = True

        for size in cube_set_sizes:
            if (
                size["red"] > color_to_maximum_cube_set_size["red"]
                or size["green"] > color_to_maximum_cube_set_size["green"]
                or size["blue"] > color_to_maximum_cube_set_size["blue"]
            ):
                is_possible = False

                break

        if is_possible:
            possible_game_ids_sum += id

    print(f"Part 1 Puzzle Answer: {possible_game_ids_sum}")


def solve_part_two(input: str) -> None:
    minimum_cube_set_powers_sum = 0

    for _, cube_set_sizes in parse_game_records(input):
        color_to_minimum_cube_set_size: CubeSetSizesByColor = {"red": 0, "green": 0, "blue": 0}

        for size in cube_set_sizes:
            if size["red"] > color_to_minimum_cube_set_size["red"]:
                color_to_minimum_cube_set_size["red"] = size["red"]

            if size["green"] > color_to_minimum_cube_set_size["green"]:
                color_to_minimum_cube_set_size["green"] = size["green"]

            if size["blue"] > color_to_minimum_cube_set_size["blue"]:
                color_to_minimum_cube_set_size["blue"] = size["blue"]

        minimum_cube_set_powers_sum += (
            color_to_minimum_cube_set_size["red"]
            * color_to_minimum_cube_set_size["green"]
            * color_to_minimum_cube_set_size["blue"]
        )

    print(f"Part 2 Puzzle Answer: {minimum_cube_set_powers_sum}")


def main() -> None:
    print("--- Day 2: Cube Conundrum ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
