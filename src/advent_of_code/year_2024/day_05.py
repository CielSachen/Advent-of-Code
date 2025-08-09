TITLE = "Print Queue"

type _PageOrderingRule = tuple[int, ...]
type _Update = list[int]


def _parse_safety_protocols(puzzle_in: str) -> tuple[list[_PageOrderingRule], list[_Update]]:
    page_ordering_rules: list[_PageOrderingRule] = []
    updates: list[_Update] = []

    for line in puzzle_in.splitlines():
        if "|" in line:
            page_ordering_rules.append(tuple(map(int, line.split("|", maxsplit=1))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return page_ordering_rules, updates


def _get_update_rules(update: _Update, page_ordering_rules: list[_PageOrderingRule]) -> list[_PageOrderingRule]:
    return [
        (first_page, second_page)
        for first_page, second_page in page_ordering_rules
        if first_page in update and second_page in update
    ]


def _is_correct_update(update: _Update, page_ordering_rules: list[_PageOrderingRule]) -> bool:
    return all(update.index(first_page) <= update.index(second_page) for first_page, second_page in page_ordering_rules)


def solve_part_1(puzzle_in: str) -> int:
    page_ordering_rules, updates = _parse_safety_protocols(puzzle_in)

    return sum(
        update[len(update) // 2]
        for update in updates
        if _is_correct_update(update, _get_update_rules(update, page_ordering_rules))
    )


def solve_part_2(puzzle_in: str) -> int:
    page_ordering_rules, updates = _parse_safety_protocols(puzzle_in)

    correctable_updates = [
        update for update in updates if not _is_correct_update(update, _get_update_rules(update, page_ordering_rules))
    ]

    for update in correctable_updates:
        relevant_rules = _get_update_rules(update, page_ordering_rules)

        while not _is_correct_update(update, relevant_rules):
            for first_page, second_page in relevant_rules:
                if (first_page_idx := update.index(first_page)) > (second_page_idx := update.index(second_page)):
                    update[first_page_idx], update[second_page_idx] = (update[second_page_idx], update[first_page_idx])

    return sum(update[len(update) // 2] for update in correctable_updates)
