#!/usr/bin/env python3


def is_correct(update: list[int], page_ordering_rules: list[tuple[int, int]]) -> bool:
    for x, y in page_ordering_rules:
        if update.index(x) > update.index(y):
            return False

    return True


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 5 -----\n")

    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    input_file.close()

    updates = [list(map(int, line.split(","))) for line in lines if "," in line]
    page_ordering_rules = [list(map(int, line.split("|"))) for line in lines if "|" in line]
    correct_updates: list[list[int]] = []

    for update in updates:
        relevant_rules = [(x, y) for x, y in page_ordering_rules if x in update and y in update]

        if is_correct(update, relevant_rules):
            correct_updates.append(update)

    middle_numbers = [update[len(update) // 2] for update in correct_updates]

    print(f"Part 1 Puzzle Answer: {sum(middle_numbers)}")

    incorrect_updates = [update for update in updates if update not in correct_updates]

    for update in incorrect_updates:
        relevant_rules = [(x, y) for x, y in page_ordering_rules if x in update and y in update]

        while not is_correct(update, relevant_rules):
            for x, y in relevant_rules:
                x_index = update.index(x)
                y_index = update.index(y)

                if x_index > y_index:
                    update[x_index], update[y_index] = (
                        update[y_index],
                        update[x_index],
                    )

    new_middle_numbers = [update[len(update) // 2] for update in incorrect_updates]

    print(f"Part 2 Puzzle Answer: {sum(new_middle_numbers)}")


if __name__ == "__main__":
    main()
