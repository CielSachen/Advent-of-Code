import enum

TITLE = "Bridge Repair"


def _get_equation_expressions(equation: str) -> tuple[int, int, list[int]]:
    test_val, operands = equation.split(": ", maxsplit=1)
    first_operand, *remaining_operands = map(int, operands.split())

    return int(test_val), first_operand, remaining_operands


class _Operation(enum.StrEnum):
    ADDITION = "+"
    MULTIPLICATION = "*"
    CONCATENATION = "||"


_REGULAR_OPERATIONS = (_Operation.ADDITION, _Operation.MULTIPLICATION)


def _is_possible(
    curr_val: int, remaining_vals: list[int], op: _Operation, test_val: int, *, concatenate: bool = False
) -> bool:
    if curr_val > test_val:
        return False
    if not remaining_vals and curr_val == test_val:
        return True
    if not remaining_vals:
        return False

    next_val: int

    if op is _Operation.ADDITION:
        next_val = curr_val + remaining_vals[0]
    elif op is _Operation.MULTIPLICATION:
        next_val = curr_val * remaining_vals[0]
    else:
        next_val = int(str(curr_val) + str(remaining_vals[0]))

    if concatenate:
        return any(_is_possible(next_val, remaining_vals[1:], op, test_val, concatenate=True) for op in _Operation)

    return any(_is_possible(next_val, remaining_vals[1:], op, test_val) for op in _REGULAR_OPERATIONS)


def solve_part_1(puzzle_in: str) -> int:
    possible_test_vals_sum = 0

    for equation in puzzle_in.splitlines():
        test_val, first_operand, remaining_operands = _get_equation_expressions(equation)

        if any(_is_possible(first_operand, remaining_operands, op, test_val) for op in _REGULAR_OPERATIONS):
            possible_test_vals_sum += test_val

    return possible_test_vals_sum


def solve_part_2(puzzle_in: str) -> int:
    possible_test_vals_sum = 0

    for equation in puzzle_in.splitlines():
        test_val, first_operand, remaining_operands = _get_equation_expressions(equation)

        if any(_is_possible(first_operand, remaining_operands, op, test_val, concatenate=True) for op in _Operation):
            possible_test_vals_sum += test_val

    return possible_test_vals_sum
