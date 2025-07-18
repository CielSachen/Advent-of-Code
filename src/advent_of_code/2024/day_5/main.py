from os import path

type PageOrderingRule = tuple[int, ...]
type Update = list[int]


def parse_safety_protocols(puzzle_in: str) -> tuple[list[PageOrderingRule], list[Update]]:
    page_ordering_rules: list[PageOrderingRule] = []
    updates: list[Update] = []

    for line in puzzle_in.splitlines():
        if "|" in line:
            page_ordering_rules.append(tuple(map(int, line.split("|", maxsplit=1))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return page_ordering_rules, updates


def get_relevant_rules(page_ordering_rules: list[PageOrderingRule], update: Update) -> list[PageOrderingRule]:
    return [
        (first_page, second_page)
        for first_page, second_page in page_ordering_rules
        if first_page in update and second_page in update
    ]


def is_correct_update(update: Update, page_ordering_rules: list[PageOrderingRule]) -> bool:
    return all(update.index(first_page) <= update.index(second_page) for first_page, second_page in page_ordering_rules)


def solve_part_one(puzzle_in: str) -> None:
    page_ordering_rules, updates = parse_safety_protocols(puzzle_in)

    correct_updates = [u for u in updates if is_correct_update(u, get_relevant_rules(page_ordering_rules, u))]

    middle_page_nums_sum = 0

    for update in correct_updates:
        middle_page_nums_sum += update[len(update) // 2]

    print(f"Part 1 Puzzle Answer: {middle_page_nums_sum}")


def solve_part_two(puzzle_in: str) -> None:
    page_ordering_rules, updates = parse_safety_protocols(puzzle_in)

    correctable_updates = [u for u in updates if not is_correct_update(u, get_relevant_rules(page_ordering_rules, u))]

    for update in correctable_updates:
        relevant_rules = get_relevant_rules(page_ordering_rules, update)

        while not is_correct_update(update, relevant_rules):
            for first_page, second_page in relevant_rules:
                first_page_idx = update.index(first_page)
                second_page_idx = update.index(second_page)

                if first_page_idx > second_page_idx:
                    update[first_page_idx], update[second_page_idx] = (update[second_page_idx], update[first_page_idx])

    middle_page_nums_sum = 0

    for update in correctable_updates:
        middle_page_nums_sum += update[len(update) // 2]

    print(f"Part 2 Puzzle Answer: {middle_page_nums_sum}")


def main() -> None:
    print("--- Day 5: Print Queue ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
