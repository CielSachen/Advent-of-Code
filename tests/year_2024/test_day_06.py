import textwrap

from advent_of_code.year_2024 import day_06


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("""\
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
    """)

    def test_part_1(self) -> None:
        assert day_06.solve_part_1(self.__PUZZLE_INPUT) == 41

    def test_part_2(self) -> None:
        assert day_06.solve_part_2(self.__PUZZLE_INPUT) == 6
