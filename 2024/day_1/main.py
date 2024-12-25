#!/usr/bin/env python3


def get_numbers(number_pairs: list[str]) -> tuple[list[int], list[int]]:
    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for pair in number_pairs:
        numbers = tuple(map(int, pair.split(maxsplit=1)))

        left_numbers.append(numbers[0])
        right_numbers.append(numbers[1])

    return left_numbers, right_numbers


def solve_part_one(input: str) -> None:
    left_numbers, right_numbers = get_numbers(input.splitlines())

    left_numbers.sort()
    right_numbers.sort()

    distances = [abs(left_number - right_number) for left_number, right_number in zip(left_numbers, right_numbers)]

    print(f"Part 1 Puzzle Answer: {sum(distances)}")


def solve_part_two(input: str) -> None:
    left_numbers, right_numbers = get_numbers(input.splitlines())
    similarity_score = 0

    for left_number in left_numbers:
        similarity_score += left_number * right_numbers.count(left_number)

    print(f"Part 2 Puzzle Answer: {similarity_score}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 1 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
