from enum import Enum, auto
from os import path


def get_equation_expressions(equation: str) -> tuple[int, int, list[int]]:
    test_val, operands = equation.split(": ", maxsplit=1)
    first_operand, *remaining_operands = map(int, operands.split())

    return int(test_val), first_operand, remaining_operands


class Operation(Enum):
    ADDITION = auto()
    MULTIPLICATION = auto()
    CONCATENATION = auto()


REGULAR_OPERATIONS = (Operation.ADDITION, Operation.MULTIPLICATION)


def is_possible(
    curr_val: int,
    remaining_vals: list[int],
    operation: Operation,
    test_val: int,
    concatenate: bool = False,  # noqa: FBT001, FBT002
) -> bool:
    if curr_val > test_val:
        return False
    if not remaining_vals and curr_val == test_val:
        return True
    if not remaining_vals:
        return False

    next_val: int

    if operation is Operation.ADDITION:
        next_val = curr_val + remaining_vals[0]
    elif operation is Operation.MULTIPLICATION:
        next_val = curr_val * remaining_vals[0]
    else:
        next_val = int(str(curr_val) + str(remaining_vals[0]))

    if concatenate:
        return any(is_possible(next_val, remaining_vals[1:], o, test_val, concatenate) for o in Operation)

    return any(is_possible(next_val, remaining_vals[1:], o, test_val) for o in REGULAR_OPERATIONS)


def solve_part_one(puzzle_in: str) -> None:
    possible_test_vals_sum = 0

    for equation in puzzle_in.splitlines():
        test_val, first_operand, remaining_operands = get_equation_expressions(equation)

        if any(is_possible(first_operand, remaining_operands, o, test_val) for o in REGULAR_OPERATIONS):
            possible_test_vals_sum += test_val

    print(f"Part 1 Puzzle Answer: {possible_test_vals_sum}")


def solve_part_two(puzzle_in: str) -> None:
    possible_test_vals_sum = 0

    for equation in puzzle_in.splitlines():
        test_val, first_operand, remaining_operands = get_equation_expressions(equation)

        if any(is_possible(first_operand, remaining_operands, o, test_val, concatenate=True) for o in Operation):
            possible_test_vals_sum += test_val

    print(f"Part 2 Puzzle Answer: {possible_test_vals_sum}")


def main() -> None:
    print("--- Day 7: Bridge Repair ---")

    print()

    with open(path.join(path.dirname(__file__), "input.txt")) as f:
        puzzle_in = f.read()

    solve_part_one(puzzle_in)

    solve_part_two(puzzle_in)


if __name__ == "__main__":
    main()
