#!/usr/bin/env python3

type OrderedPairLike = list[int]
type OrderedPair = tuple[int, int]


def parse_safety_protocols(
    safety_protocols: list[str],
) -> tuple[list[OrderedPairLike], list[OrderedPairLike]]:
    updates: list[OrderedPairLike] = []
    page_ordering_rules: list[OrderedPairLike] = []

    for line in safety_protocols:
        if "," in line:
            updates.append(list(map(int, line.split(","))))
        elif "|" in line:
            page_ordering_rules.append(list(map(int, line.split("|", maxsplit=1))))

    return updates, page_ordering_rules


def get_relevant_rules(
    update: OrderedPairLike, page_ordering_rules: list[OrderedPairLike]
) -> list[OrderedPair]:
    return [
        (first_page, second_page)
        for first_page, second_page in page_ordering_rules
        if first_page in update and second_page in update
    ]


def is_correct_update(update: OrderedPairLike, page_ordering_rules: list[OrderedPair]) -> bool:
    for first_page, second_page in page_ordering_rules:
        if update.index(first_page) > update.index(second_page):
            return False

    return True


def solve_part_one(input: str) -> None:
    safety_protocols = input.splitlines()
    updates, page_ordering_rules = parse_safety_protocols(safety_protocols)
    correct_updates: list[OrderedPairLike] = []

    for update in updates:
        if is_correct_update(update, get_relevant_rules(update, page_ordering_rules)):
            correct_updates.append(update)

    middle_page_numbers_sum = 0

    for update in correct_updates:
        middle_page_numbers_sum += update[len(update) // 2]

    print(f"Part 1 Puzzle Answer: {middle_page_numbers_sum}")


def solve_part_two(input: str) -> None:
    safety_protocols = input.splitlines()
    updates, page_ordering_rules = parse_safety_protocols(safety_protocols)
    correctable_updates: list[OrderedPairLike] = []

    for update in updates:
        if not is_correct_update(update, get_relevant_rules(update, page_ordering_rules)):
            correctable_updates.append(update)

    for update in correctable_updates:
        relevant_rules = get_relevant_rules(update, page_ordering_rules)

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
    print("----- ADVENT OF CODE : 2024 : DAY 5 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
