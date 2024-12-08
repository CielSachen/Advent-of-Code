#!/usr/bin/env python3


def is_correct(update: list[int], page_ordering_rules: list[tuple[int, int]]) -> bool:
    for first_page, second_page in page_ordering_rules:
        if update.index(first_page) > update.index(second_page):
            return False

    return True


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 5 -----\n")

    with open("input.txt", "r") as input_file:
        lines = input_file.read().splitlines()

    updates = [list(map(int, line.split(","))) for line in lines if "," in line]
    page_ordering_rules = [list(map(int, line.split("|", 1))) for line in lines if "|" in line]
    correct_updates: list[list[int]] = []

    for update in updates:
        relevant_rules = [
            (first_page, second_page)
            for first_page, second_page in page_ordering_rules
            if first_page in update and second_page in update
        ]

        if is_correct(update, relevant_rules):
            correct_updates.append(update)

    middle_pages = [update[len(update) // 2] for update in correct_updates]

    print(f"Part 1 Puzzle Answer: {sum(middle_pages)}")

    incorrect_updates = [update for update in updates if update not in correct_updates]

    for update in incorrect_updates:
        relevant_rules = [
            (first_page, second_page)
            for first_page, second_page in page_ordering_rules
            if first_page in update and second_page in update
        ]

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


if __name__ == "__main__":
    main()
