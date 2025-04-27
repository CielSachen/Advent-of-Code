#!/usr/bin/env python3

from enum import Enum, auto
from os import path


def get_equation_expressions(equation: str) -> tuple[int, int, list[int]]:
    test_value, operands = equation.split(": ", maxsplit=1)
    first_operand, *remaining_operands = list(map(int, operands.split()))

    return int(test_value), first_operand, remaining_operands


class Operation(Enum):
    ADDITION = auto()
    MULTIPLICATION = auto()
    CONCATENATION = auto()


def is_possible(
    current_value: int,
    remaining_values: list[int],
    operation: Operation,
    test_value: int,
    should_concatenate: bool = False,
) -> bool:
    if current_value > test_value:
        return False
    elif not remaining_values and current_value == test_value:
        return True
    elif not remaining_values:
        return False

    if operation == Operation.ADDITION:
        current_value = current_value + remaining_values[0]
    elif operation == Operation.MULTIPLICATION:
        current_value = current_value * remaining_values[0]
    else:
        current_value = int(str(current_value) + str(remaining_values[0]))

    if should_concatenate:
        return (
            is_possible(
                current_value,
                remaining_values[1:],
                Operation.ADDITION,
                test_value,
                should_concatenate=True,
            )
            or is_possible(
                current_value,
                remaining_values[1:],
                Operation.MULTIPLICATION,
                test_value,
                should_concatenate=True,
            )
            or is_possible(
                current_value,
                remaining_values[1:],
                Operation.CONCATENATION,
                test_value,
                should_concatenate=True,
            )
        )

    return is_possible(
        current_value, remaining_values[1:], Operation.ADDITION, test_value
    ) or is_possible(current_value, remaining_values[1:], Operation.MULTIPLICATION, test_value)


def solve_part_one(input: str) -> None:
    possible_test_values_sum = 0

    for equation in input.splitlines():
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if is_possible(
            first_operand, remaining_operands, Operation.ADDITION, test_value
        ) or is_possible(first_operand, remaining_operands, Operation.MULTIPLICATION, test_value):
            possible_test_values_sum += test_value

    print(f"Part 1 Puzzle Answer: {possible_test_values_sum}")


def solve_part_two(input: str) -> None:
    possible_test_values_sum = 0

    for equation in input.splitlines():
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if (
            is_possible(
                first_operand,
                remaining_operands,
                Operation.ADDITION,
                test_value,
                should_concatenate=True,
            )
            or is_possible(
                first_operand,
                remaining_operands,
                Operation.MULTIPLICATION,
                test_value,
                should_concatenate=True,
            )
            or is_possible(
                first_operand,
                remaining_operands,
                Operation.CONCATENATION,
                test_value,
                should_concatenate=True,
            )
        ):
            possible_test_values_sum += test_value

    print(f"Part 2 Puzzle Answer: {possible_test_values_sum}")


def main() -> None:
    print("--- Day 7: Bridge Repair ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt"), mode="r") as input_file:
        puzzle_input = input_file.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
