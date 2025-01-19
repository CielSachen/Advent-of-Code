#!/usr/bin/env python3

from collections import defaultdict

type CubeSetSize = dict[str, int]

GAME_RECORD_SEPARATOR = {"colon": ": ", "semi_colon": "; ", "comma": ", "}
MAXIMUM_CUBE_SET_SIZE = {"red": 12, "green": 13, "blue": 14}


def get_game_records(
    raw_game_records: list[list[str]],
) -> list[tuple[int, list[CubeSetSize]]]:
    game_records: list[tuple[int, list[CubeSetSize]]] = []

    for raw_record in raw_game_records:
        raw_id, raw_cube_sets = raw_record
        cube_set_sizes: list[CubeSetSize] = []

        for raw_set in raw_cube_sets.split(GAME_RECORD_SEPARATOR["semi_colon"]):
            set_size: defaultdict[str, int] = defaultdict(int)

            for entry in raw_set.split(GAME_RECORD_SEPARATOR["comma"]):
                size, color = entry.split(maxsplit=1)
                set_size[color] = int(size)

            cube_set_sizes.append(set_size)

        game_records.append((int(raw_id.replace("Game ", "")), cube_set_sizes))

    return game_records


def solve_part_one(input: str) -> None:
    raw_game_records = [
        line.split(GAME_RECORD_SEPARATOR["colon"], maxsplit=1) for line in input.splitlines()
    ]
    game_records = get_game_records(raw_game_records)
    possible_game_ids_sum = 0

    for id, cube_set_sizes in game_records:
        is_possible = True

        for size in cube_set_sizes:
            if (
                size["red"] > MAXIMUM_CUBE_SET_SIZE["red"]
                or size["green"] > MAXIMUM_CUBE_SET_SIZE["green"]
                or size["blue"] > MAXIMUM_CUBE_SET_SIZE["blue"]
            ):
                is_possible = False

                break

        if is_possible:
            possible_game_ids_sum += id

    print(f"Part 1 Puzzle Answer: {possible_game_ids_sum}")


def solve_part_two(input: str) -> None:
    raw_game_records = [
        line.split(GAME_RECORD_SEPARATOR["colon"], maxsplit=1) for line in input.splitlines()
    ]
    game_records = get_game_records(raw_game_records)
    minimum_cube_set_powers_sum = 0

    for _, cube_set_sizes in game_records:
        minimum_cube_set_size = {"red": 0, "green": 0, "blue": 0}

        for size in cube_set_sizes:
            if size["red"] > minimum_cube_set_size["red"]:
                minimum_cube_set_size["red"] = size["red"]

            if size["green"] > minimum_cube_set_size["green"]:
                minimum_cube_set_size["green"] = size["green"]

            if size["blue"] > minimum_cube_set_size["blue"]:
                minimum_cube_set_size["blue"] = size["blue"]

        minimum_cube_set_powers_sum += (
            minimum_cube_set_size["red"]
            * minimum_cube_set_size["green"]
            * minimum_cube_set_size["blue"]
        )

    print(f"Part 2 Puzzle Answer: {minimum_cube_set_powers_sum}")


def main() -> None:
    print("----- ADVENT OF CODE : 2023 : DAY 2 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
