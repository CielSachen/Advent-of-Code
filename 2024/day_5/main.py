#!/usr/bin/env python3

type OrderedPair = tuple[int, int]
type OrderedPairLike = list[int]


def get_relevant_rules(update: OrderedPairLike, page_ordering_rules: list[OrderedPairLike]) -> list[OrderedPair]:
    return [
        (first_page, second_page)
        for first_page, second_page in page_ordering_rules
        if first_page in update and second_page in update
    ]


def is_correct(update: OrderedPairLike, page_ordering_rules: list[OrderedPair]) -> bool:
    for first_page, second_page in page_ordering_rules:
        if update.index(first_page) > update.index(second_page):
            return False

    return True


def solve_part_one(input: str) -> None:
    input_lines = input.splitlines()
    updates = [list(map(int, line.split(","))) for line in input_lines if "," in line]
    page_ordering_rules = [list(map(int, line.split("|", 1))) for line in input_lines if "|" in line]
    correct_updates: list[OrderedPairLike] = []

    for update in updates:
        relevant_rules = get_relevant_rules(update, page_ordering_rules)

        if is_correct(update, relevant_rules):
            correct_updates.append(update)

    middle_pages = [update[len(update) // 2] for update in correct_updates]

    print(f"Part 1 Puzzle Answer: {sum(middle_pages)}")


def solve_part_two(input: str) -> None:
    input_lines = input.splitlines()
    updates = [list(map(int, line.split(","))) for line in input_lines if "," in line]
    page_ordering_rules = [list(map(int, line.split("|", 1))) for line in input_lines if "|" in line]
    incorrect_updates: list[OrderedPairLike] = []

    for update in updates:
        relevant_rules = get_relevant_rules(update, page_ordering_rules)

        if not is_correct(update, relevant_rules):
            incorrect_updates.append(update)

    for update in incorrect_updates:
        relevant_rules = get_relevant_rules(update, page_ordering_rules)

        while not is_correct(update, relevant_rules):
            for first_page, second_page in relevant_rules:
                first_page_index = update.index(first_page)
                second_page_index = update.index(second_page)

                if first_page_index > second_page_index:
                    update[first_page_index], update[second_page_index] = (
                        update[second_page_index],
                        update[first_page_index],
                    )

    middle_pages = [update[len(update) // 2] for update in incorrect_updates]

    print(f"Part 2 Puzzle Answer: {sum(middle_pages)}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 5 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
