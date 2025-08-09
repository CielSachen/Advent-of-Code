import textwrap

from advent_of_code.year_2024 import day_09


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("2333133121414131402")

    def test_part_1(self) -> None:
        assert day_09.solve_part_1(self.__PUZZLE_INPUT) == 1928

    def test_part_2(self) -> None:
        assert day_09.solve_part_2(self.__PUZZLE_INPUT) == 2858
