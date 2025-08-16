import textwrap

from advent_of_code.year_2024 import day_07


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("""\
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
    """)

    def test_part_1(self) -> None:
        assert day_07.solve_part_1(self.__PUZZLE_INPUT) == 3749

    def test_part_2(self) -> None:
        assert day_07.solve_part_2(self.__PUZZLE_INPUT) == 11387
