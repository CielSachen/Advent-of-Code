#!/usr/bin/env python3


from typing import Literal


def is_possible(
    current_value: int,
    remaining_operands: list[int],
    test_value: int,
    operation: Literal["+", "*", "||"],
    concatenate: bool = False,
) -> bool:
    if current_value > test_value:
        return False
    elif not remaining_operands and current_value == test_value:
        return True
    elif not remaining_operands:
        return False

    if operation == "+":
        current_value = current_value + remaining_operands[0]
    elif operation == "*":
        current_value = current_value * remaining_operands[0]
    else:
        current_value = int(str(current_value) + str(remaining_operands[0]))

    if concatenate:
        return (
            is_possible(current_value, remaining_operands[1:], test_value, "+", True)
            or is_possible(current_value, remaining_operands[1:], test_value, "*", True)
            or is_possible(current_value, remaining_operands[1:], test_value, "||", True)
        )

    return is_possible(current_value, remaining_operands[1:], test_value, "+") or is_possible(
        current_value, remaining_operands[1:], test_value, "*"
    )


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 7 -----\n")

    with open("input.txt", "r") as input_file:
        equations = input_file.read().splitlines()

    initial_possible_test_values: list[int] = []
    actual_possible_test_values: list[int] = []

    for equation in equations:
        test_value, operands = equation.split(":", 1)
        test_value = int(test_value)
        first_operand, *remaining_operands = list(map(int, operands.split()))

        if is_possible(first_operand, remaining_operands, test_value, "+") or is_possible(
            first_operand, remaining_operands, test_value, "*"
        ):
            initial_possible_test_values.append(test_value)

        if (
            is_possible(first_operand, remaining_operands, test_value, "+", True)
            or is_possible(first_operand, remaining_operands, test_value, "*", True)
            or is_possible(first_operand, remaining_operands, test_value, "||", True)
        ):
            actual_possible_test_values.append(test_value)

    print(f"Part 1 Puzzle Answer: {sum(initial_possible_test_values)}")
    print(f"Part 2 Puzzle Answer: {sum(actual_possible_test_values)}")


if __name__ == "__main__":
    main()
