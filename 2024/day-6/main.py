#!/usr/bin/env python3

POSITION_DELTAS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def get_starting_position(rows: list[str]) -> tuple[int, int]:
    for index, row in enumerate(rows):
        if "^" in row:
            return (row.index("^"), index)

    raise Exception("The caret (^) character representing the starting position does not exist.")


def get_visited_positions_amount(
    rows: list[str], starting_position: tuple[int, int], additional_block_position: tuple[int, int] | None = None
) -> set[tuple[int, int]]:
    current_position = starting_position
    current_direction = 0
    visited_positions = {starting_position}
    directional_visited_positions: set[tuple[tuple[int, int], int]] = set()

    while True:
        next_position_x = current_position[0] + POSITION_DELTAS[current_direction][0]
        next_position_y = current_position[1] + POSITION_DELTAS[current_direction][1]

        if (
            next_position_x < 0
            or next_position_y < 0
            or next_position_x >= len(rows[0])
            or next_position_y >= len(rows)
        ):
            break

        if (
            rows[next_position_y][next_position_x] == "#"
            or (next_position_x, next_position_y) == additional_block_position
        ):
            current_direction = (current_direction + 1) % 4
        else:
            current_position = (next_position_x, next_position_y)

        if current_position not in visited_positions and additional_block_position is None:
            visited_positions.add(current_position)
        elif additional_block_position is not None:
            if (current_position, current_direction) not in directional_visited_positions:
                directional_visited_positions.add((current_position, current_direction))
            else:
                return set()

    return visited_positions


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 6 -----\n")

    with open("input.txt", "r") as input_file:
        rows = input_file.readlines()

    starting_position = get_starting_position(rows)
    visited_positions = get_visited_positions_amount(rows, starting_position)

    print(f"Part 1 Puzzle Answer: {len(visited_positions)}")

    new_block_positions_amount = 0

    for position in visited_positions:
        if position != starting_position and len(get_visited_positions_amount(rows, starting_position, position)) == 0:
            new_block_positions_amount += 1

    print(f"Part 2 Puzzle Answer: {new_block_positions_amount}")


if __name__ == "__main__":
    main()
