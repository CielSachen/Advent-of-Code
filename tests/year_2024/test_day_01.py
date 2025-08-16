import textwrap

from advent_of_code.year_2024 import day_01


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("""\
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
    """)

    def test_part_1(self) -> None:
        assert day_01.solve_part_1(self.__PUZZLE_INPUT) == 11

    def test_part_2(self) -> None:
        assert day_01.solve_part_2(self.__PUZZLE_INPUT) == 31
