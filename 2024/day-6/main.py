#!/usr/bin/env python3

type OrderedPair = tuple[int, int]

POSITION_DELTAS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def get_starting_position(rows: list[str]) -> OrderedPair:
    for row_number, row in enumerate(rows):
        if "^" in row:
            return (row.index("^"), row_number)

    raise Exception("The caret (^) character representing the starting position does not exist.")


def get_visited_positions_amount(
    rows: list[str], starting_position: OrderedPair, additional_block_position: OrderedPair | None = None
) -> set[OrderedPair]:
    current_position = starting_position
    current_direction = 0
    visited_positions = {starting_position}
    directional_visited_positions: set[tuple[OrderedPair, int]] = set()

    while True:
        next_position_x = current_position[0] + POSITION_DELTAS[current_direction][0]
        next_position_y = current_position[1] + POSITION_DELTAS[current_direction][1]

        if not (0 <= next_position_x < len(rows[0])) or not (0 <= next_position_y < len(rows)):
            break

        if (
            rows[next_position_y][next_position_x] == "#"
            or (next_position_x, next_position_y) == additional_block_position
        ):
            current_direction = (current_direction + 1) % 4
        else:
            current_position = (next_position_x, next_position_y)

        if not additional_block_position:
            if current_position not in visited_positions:
                visited_positions.add(current_position)
        else:
            if (current_position, current_direction) not in directional_visited_positions:
                directional_visited_positions.add((current_position, current_direction))
            else:
                return set()

    return visited_positions


def solve_part_one(input: str) -> None:
    rows = input.splitlines()
    starting_position = get_starting_position(rows)
    visited_positions = get_visited_positions_amount(rows, starting_position)

    print(f"Part 1 Puzzle Answer: {len(visited_positions)}")


def solve_part_two(input: str) -> None:
    rows = input.splitlines()
    starting_position = get_starting_position(rows)
    visited_positions = get_visited_positions_amount(rows, starting_position)
    new_block_positions_amount = 0

    for position in visited_positions:
        if position != starting_position and len(get_visited_positions_amount(rows, starting_position, position)) == 0:
            new_block_positions_amount += 1

    print(f"Part 2 Puzzle Answer: {new_block_positions_amount}")


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 6 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
