from os import path

type PageOrderingRule = tuple[int, ...]


def parse_safety_protocols(puzzle_input: str) -> tuple[list[PageOrderingRule], list[list[int]]]:
    page_ordering_rules: list[PageOrderingRule] = []
    updates: list[list[int]] = []

    for line in puzzle_input.splitlines():
        if "|" in line:
            page_ordering_rules.append(tuple(map(int, line.split("|", maxsplit=1))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return page_ordering_rules, updates


def get_relevant_rules(
    page_ordering_rules: list[PageOrderingRule], update: list[int]
) -> list[PageOrderingRule]:
    return [
        (first_page, second_page)
        for first_page, second_page in page_ordering_rules
        if first_page in update and second_page in update
    ]


def is_correct_update(update: list[int], page_ordering_rules: list[PageOrderingRule]) -> bool:
    for first_page, second_page in page_ordering_rules:
        if update.index(first_page) > update.index(second_page):
            return False

    return True


def solve_part_one(puzzle_input: str) -> None:
    page_ordering_rules, updates = parse_safety_protocols(puzzle_input)

    correct_updates = [
        update
        for update in updates
        if is_correct_update(update, get_relevant_rules(page_ordering_rules, update))
    ]

    middle_page_numbers_sum = 0

    for update in correct_updates:
        middle_page_numbers_sum += update[len(update) // 2]

    print(f"Part 1 Puzzle Answer: {middle_page_numbers_sum}")


def solve_part_two(puzzle_input: str) -> None:
    page_ordering_rules, updates = parse_safety_protocols(puzzle_input)

    correctable_updates = [
        update
        for update in updates
        if not is_correct_update(update, get_relevant_rules(page_ordering_rules, update))
    ]

    for update in correctable_updates:
        relevant_rules = get_relevant_rules(page_ordering_rules, update)

        while not is_correct_update(update, relevant_rules):
            for first_page, second_page in relevant_rules:
                first_page_index = update.index(first_page)
                second_page_index = update.index(second_page)

                if first_page_index > second_page_index:
                    update[first_page_index], update[second_page_index] = (
                        update[second_page_index],
                        update[first_page_index],
                    )

    middle_page_numbers_sum = 0

    for update in correctable_updates:
        middle_page_numbers_sum += update[len(update) // 2]

    print(f"Part 2 Puzzle Answer: {middle_page_numbers_sum}")


def main() -> None:
    print("--- Day 5: Print Queue ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
