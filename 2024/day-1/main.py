#!/usr/bin/env python3


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 1 -----\n")

    with open("input.txt", "r") as input_file:
        number_pairs = input_file.read().splitlines()

    left_number_list: list[int] = []
    right_number_list: list[int] = []

    for pair in number_pairs:
        numbers = list(map(int, pair.split(maxsplit=1)))

        left_number_list.append(numbers[0])
        right_number_list.append(numbers[1])

    left_number_list.sort()
    right_number_list.sort()

    distances = [abs(left_number_list[index] - right_number_list[index]) for index in range(len(number_pairs))]

    print(f"Part 1 Puzzle Answer: {sum(distances)}")

    similarity_score = 0

    for left_number in left_number_list:
        similarity_score += left_number * right_number_list.count(left_number)

    print(f"Part 2 Puzzle Answer: {similarity_score}")


if __name__ == "__main__":
    main()
