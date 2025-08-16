import collections

TITLE = "Disk Fragmenter"

_FREE_SPACE_KEY = "."


def _get_file_blocks(puzzle_in: str) -> list[str]:
    file_blocks: list[str] = []

    file_id = 0
    is_free_space = False

    for char in puzzle_in.strip():
        num = int(char)

        file_blocks.extend(str(file_id) if not is_free_space else _FREE_SPACE_KEY for _ in range(num))

        if is_free_space := not is_free_space:
            file_id += 1

    return file_blocks


def solve_part_1(puzzle_in: str) -> int:
    file_blocks = _get_file_blocks(puzzle_in)
    file_block_cnt = len(file_blocks)

    reverse_idx = 0

    for i, block in enumerate(file_blocks):
        if block == _FREE_SPACE_KEY and i < file_block_cnt + reverse_idx:
            while i < file_block_cnt + reverse_idx:
                if (last_file_block := file_blocks[(reverse_idx := reverse_idx - 1)]) != _FREE_SPACE_KEY:
                    file_blocks[i] = last_file_block
                    file_blocks[reverse_idx] = _FREE_SPACE_KEY

                    break

    return sum(int(block) * i for i, block in enumerate(file_blocks) if block.isdigit())


def solve_part_2(puzzle_in: str) -> int:
    file_blocks = _get_file_blocks(puzzle_in)
    file_block_cnt = len(file_blocks)

    free_spaces: dict[int, list[int]] = collections.defaultdict(list)
    free_space_cnt = 0

    free_space_idx = 0

    while free_space_idx < file_block_cnt:
        if file_blocks[free_space_idx] == _FREE_SPACE_KEY:
            free_spaces[(free_space_cnt := free_space_cnt + 1)].append(free_space_idx)

            while file_blocks[free_space_idx + 1] == _FREE_SPACE_KEY:
                free_spaces[free_space_cnt].append(free_space_idx := free_space_idx + 1)

        free_space_idx += 1

    reverse_idx = -1

    while reverse_idx >= -file_block_cnt:
        if file_blocks[reverse_idx] != _FREE_SPACE_KEY:
            reverse_indexes = [reverse_idx]

            while (reverse_idx := reverse_idx - 1) >= -file_block_cnt and file_blocks[reverse_idx] == file_blocks[
                reverse_idx + 1
            ]:
                reverse_indexes.append(reverse_idx)

            front_indexes: list[int] | None = None

            for free_space in free_spaces.values():
                if len(free_space) >= len(reverse_indexes):
                    front_indexes = free_space

                    break

            if front_indexes is not None and file_block_cnt + reverse_indexes[0] > front_indexes[0]:
                for i in reverse_indexes:
                    file_blocks[front_indexes.pop(0)] = file_blocks[i]
                    file_blocks[i] = _FREE_SPACE_KEY

            continue

        reverse_idx -= 1

    return sum(int(block) * i for i, block in enumerate(file_blocks) if block.isdigit())
