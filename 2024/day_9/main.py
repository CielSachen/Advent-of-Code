from collections import defaultdict
from os import path

FREE_SPACE = "."


def get_file_blocks(puzzle_input: str) -> list[str]:
    file_blocks: list[str] = []
    file_id = 0
    is_free_space = False

    for character in puzzle_input.strip():
        number = int(character)

        file_blocks.extend(str(file_id) if not is_free_space else FREE_SPACE for _ in range(number))

        is_free_space = not is_free_space

        if is_free_space:
            file_id += 1

    return file_blocks


def solve_part_one(puzzle_input: str) -> None:
    file_blocks = get_file_blocks(puzzle_input)
    file_block_count = len(file_blocks)

    reverse_index = 0

    for index, block in enumerate(file_blocks):
        if block == FREE_SPACE and index < file_block_count + reverse_index:
            while index < file_block_count + reverse_index:
                reverse_index -= 1
                last_file_block = file_blocks.pop()

                if last_file_block != FREE_SPACE:
                    file_blocks[index] = last_file_block

                    break

    checksum = 0

    for index, block in enumerate(file_blocks):
        checksum += int(block) * index

    print(f"Part 1 Puzzle Answer: {checksum}")


def solve_part_two(puzzle_input: str) -> None:
    file_blocks = get_file_blocks(puzzle_input)
    file_block_count = len(file_blocks)

    free_spaces: dict[int, list[int]] = defaultdict(list)
    free_space_index = 0
    free_space_count = 0

    while free_space_index < file_block_count:
        if file_blocks[free_space_index] == FREE_SPACE:
            free_space_count += 1

            free_spaces[free_space_count].append(free_space_index)

            while file_blocks[free_space_index + 1] == FREE_SPACE:
                free_space_index += 1

                free_spaces[free_space_count].append(free_space_index)

        free_space_index += 1

    reverse_index = -1

    while reverse_index >= -file_block_count:
        if file_blocks[reverse_index] != FREE_SPACE:
            reverse_indexes = [reverse_index]
            reverse_index -= 1

            while (
                reverse_index >= -file_block_count
                and file_blocks[reverse_index] == file_blocks[reverse_index + 1]
            ):
                reverse_indexes.append(reverse_index)

                reverse_index -= 1

            front_indexes: list[int] | None = None

            for free_space in free_spaces.values():
                if len(free_space) >= len(reverse_indexes):
                    front_indexes = free_space

                    break

            if (
                front_indexes is not None
                and file_block_count + reverse_indexes[0] > front_indexes[0]
            ):
                for index in reverse_indexes:
                    file_blocks[front_indexes.pop(0)] = file_blocks[index]
                    file_blocks[index] = FREE_SPACE

            continue

        reverse_index -= 1

    checksum = 0

    for index, block in enumerate(file_blocks):
        if block.isdigit():
            checksum += int(block) * index

    print(f"Part 2 Puzzle Answer: {checksum}")


def main() -> None:
    print("--- Day 9: Disk Fragmenter ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
