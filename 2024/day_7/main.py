#!/usr/bin/env python3

from enum import Enum, auto


class Operation(Enum):
    ADDITION = auto()
    MULTIPLICATION = auto()
    CONCATENATION = auto()


def get_equation_expressions(equation: str) -> tuple[int, int, list[int]]:
    test_value, operands = equation.split(": ", maxsplit=1)
    first_operand, *remaining_operands = list(map(int, operands.split()))

    return int(test_value), first_operand, remaining_operands


def is_possible(
    current_value: int,
    remaining_values: list[int],
    test_value: int,
    operation: Operation,
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
                test_value,
                Operation.ADDITION,
                should_concatenate=True,
            )
            or is_possible(
                current_value,
                remaining_values[1:],
                test_value,
                Operation.MULTIPLICATION,
                should_concatenate=True,
            )
            or is_possible(
                current_value,
                remaining_values[1:],
                test_value,
                Operation.CONCATENATION,
                should_concatenate=True,
            )
        )

    return is_possible(
        current_value, remaining_values[1:], test_value, Operation.ADDITION
    ) or is_possible(current_value, remaining_values[1:], test_value, Operation.MULTIPLICATION)


def solve_part_one(input: str) -> None:
    equations = input.splitlines()
    possible_test_values_sum = 0

    for equation in equations:
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if is_possible(
            first_operand, remaining_operands, test_value, Operation.ADDITION
        ) or is_possible(first_operand, remaining_operands, test_value, Operation.MULTIPLICATION):
            possible_test_values_sum += test_value

    print(f"Part 1 Puzzle Answer: {possible_test_values_sum}")


def solve_part_two(input: str) -> None:
    equations = input.splitlines()
    possible_test_values_sum = 0

    for equation in equations:
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if (
            is_possible(
                first_operand,
                remaining_operands,
                test_value,
                operation=Operation.ADDITION,
                should_concatenate=True,
            )
            or is_possible(
                first_operand,
                remaining_operands,
                test_value,
                operation=Operation.MULTIPLICATION,
                should_concatenate=True,
            )
            or is_possible(
                first_operand,
                remaining_operands,
                test_value,
                operation=Operation.CONCATENATION,
                should_concatenate=True,
            )
        ):
            possible_test_values_sum += test_value

    print(f"Part 2 Puzzle Answer: {possible_test_values_sum}")


def main() -> None:
    print("----- ADVENT OF CODE : 2024 : DAY 7 -----\n")

    with open("input.txt", mode="r") as input_file:
        input_file = input_file.read()

    solve_part_one(input_file)
    solve_part_two(input_file)


if __name__ == "__main__":
    main()
