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


REGULAR_OPERATIONS = (Operation.ADDITION, Operation.MULTIPLICATION)


def is_possible(
    current_value: int,
    remaining_values: list[int],
    operation: Operation,
    test_value: int,
    is_concatenating: bool = False,  # noqa: FBT001, FBT002
) -> bool:
    if current_value > test_value:
        return False
    if not remaining_values and current_value == test_value:
        return True
    if not remaining_values:
        return False

    next_value: int

    if operation is Operation.ADDITION:
        next_value = current_value + remaining_values[0]
    elif operation is Operation.MULTIPLICATION:
        next_value = current_value * remaining_values[0]
    else:
        next_value = int(str(current_value) + str(remaining_values[0]))

    if is_concatenating:
        return any(
            is_possible(next_value, remaining_values[1:], new_operation, test_value, is_concatenating)
            for new_operation in list(Operation)
        )

    return any(
        is_possible(next_value, remaining_values[1:], new_operation, test_value) for new_operation in REGULAR_OPERATIONS
    )


def solve_part_one(puzzle_input: str) -> None:
    possible_test_values_sum = 0

    for equation in puzzle_input.splitlines():
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if any(
            is_possible(first_operand, remaining_operands, operation, test_value) for operation in REGULAR_OPERATIONS
        ):
            possible_test_values_sum += test_value

    print(f"Part 1 Puzzle Answer: {possible_test_values_sum}")


def solve_part_two(puzzle_input: str) -> None:
    possible_test_values_sum = 0

    for equation in puzzle_input.splitlines():
        test_value, first_operand, remaining_operands = get_equation_expressions(equation)

        if any(
            is_possible(first_operand, remaining_operands, operation, test_value, is_concatenating=True)
            for operation in list(Operation)
        ):
            possible_test_values_sum += test_value

    print(f"Part 2 Puzzle Answer: {possible_test_values_sum}")


def main() -> None:
    print("--- Day 7: Bridge Repair ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_input = f.read()

    solve_part_one(puzzle_input)

    solve_part_two(puzzle_input)


if __name__ == "__main__":
    main()
