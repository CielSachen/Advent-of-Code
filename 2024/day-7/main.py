#!/usr/bin/env python3


from typing import Literal


def get_equation_expressions(equation: str) -> tuple[int, int, list[int]]:
    test_value, operands = equation.split(": ", 1)
    first_operand, *remaining_operands = list(map(int, operands.split()))

    return int(test_value), first_operand, remaining_operands


def is_possible(
    current_value: int,
    remaining_values: list[int],
    test_value: int,
    operation: Literal["+", "*", "||"],
    is_concatenating: bool = False,
) -> bool:
    if current_value > test_value:
        return False
    elif not remaining_values and current_value == test_value:
        return True
    elif not remaining_values:
        return False

    if operation == "+":
        current_value = current_value + remaining_values[0]
    elif operation == "*":
        current_value = current_value * remaining_values[0]
    else:
        current_value = int(str(current_value) + str(remaining_values[0]))

    if is_concatenating:
        return (
            is_possible(current_value, remaining_values[1:], test_value, "+", True)
            or is_possible(current_value, remaining_values[1:], test_value, "*", True)
            or is_possible(current_value, remaining_values[1:], test_value, "||", True)
        )

    return is_possible(current_value, remaining_values[1:], test_value, "+") or is_possible(
        current_value, remaining_values[1:], test_value, "*"
    )


def solve_part_one(input: str) -> None:
    equations = input.splitlines()
    possible_test_values: list[int] = []

    for equation in equations:
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if is_possible(first_operand, remaining_operands, test_value, "+") or is_possible(
            first_operand, remaining_operands, test_value, "*"
        ):
            possible_test_values.append(test_value)

    print(f"Part 1 Puzzle Answer: {sum(possible_test_values)}")


def solve_part_two(input: str) -> None:
    equations = input.splitlines()
    possible_test_values: list[int] = []

    for equation in equations:
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if (
            is_possible(first_operand, remaining_operands, test_value, "+", True)
            or is_possible(first_operand, remaining_operands, test_value, "*", True)
            or is_possible(first_operand, remaining_operands, test_value, "||", True)
        ):
            possible_test_values.append(test_value)

    print(f"Part 2 Puzzle Answer: {sum(possible_test_values)}")


def main():
    print("----- ADVENT OF CODE : 2024 : DAY 7 -----\n")

    with open("input.txt", "r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
