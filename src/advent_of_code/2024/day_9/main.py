from collections import defaultdict
from os import path

FREE_SPACE_KEY = "."


def get_file_blocks(puzzle_in: str) -> list[str]:
    file_blocks: list[str] = []
    file_id = 0
    is_free_space = False

    for char in puzzle_in.strip():
        num = int(char)

        file_blocks.extend(str(file_id) if not is_free_space else FREE_SPACE_KEY for _ in range(num))

        if is_free_space := not is_free_space:
            file_id += 1

    return file_blocks


def solve_part_one(puzzle_in: str) -> None:
    file_blocks = get_file_blocks(puzzle_in)
    file_block_cnt = len(file_blocks)

    removed_block_cnt = 0

    for i, block in enumerate(file_blocks):
        if block == FREE_SPACE_KEY and i < file_block_cnt - removed_block_cnt:
            while i < file_block_cnt - removed_block_cnt:
                removed_block_cnt += 1

                last_file_block = file_blocks.pop()

                if last_file_block != FREE_SPACE_KEY:
                    file_blocks[i] = last_file_block

                    break

    checksum = 0

    for i, block in enumerate(file_blocks):
        checksum += int(block) * i

    print(f"Part 1 Puzzle Answer: {checksum}")


def solve_part_two(puzzle_in: str) -> None:
    file_blocks = get_file_blocks(puzzle_in)
    file_block_cnt = len(file_blocks)

    free_spaces: dict[int, list[int]] = defaultdict(list)
    free_space_idx = 0
    free_space_cnt = 0

    while free_space_idx < file_block_cnt:
        if file_blocks[free_space_idx] == FREE_SPACE_KEY:
            free_space_cnt += 1

            free_spaces[free_space_cnt].append(free_space_idx)

            while file_blocks[free_space_idx + 1] == FREE_SPACE_KEY:
                free_space_idx += 1

                free_spaces[free_space_cnt].append(free_space_idx)

        free_space_idx += 1

    reverse_idx = -1

    while reverse_idx >= -file_block_cnt:
        if file_blocks[reverse_idx] != FREE_SPACE_KEY:
            reverse_indexes = [reverse_idx]
            reverse_idx -= 1

            while reverse_idx >= -file_block_cnt and file_blocks[reverse_idx] == file_blocks[reverse_idx + 1]:
                reverse_indexes.append(reverse_idx)

                reverse_idx -= 1

            front_indexes: list[int] | None = None

            for free_space in free_spaces.values():
                if len(free_space) >= len(reverse_indexes):
                    front_indexes = free_space

                    break

            if front_indexes is not None and file_block_cnt + reverse_indexes[0] > front_indexes[0]:
                for i in reverse_indexes:
                    file_blocks[front_indexes.pop(0)] = file_blocks[i]
                    file_blocks[i] = FREE_SPACE_KEY

            continue

        reverse_idx -= 1

    checksum = 0

    for i, block in enumerate(file_blocks):
        if block.isdigit():
            checksum += int(block) * i

    print(f"Part 2 Puzzle Answer: {checksum}")


def main() -> None:
    print("--- Day 9: Disk Fragmenter ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
