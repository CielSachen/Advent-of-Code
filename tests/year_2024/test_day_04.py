import textwrap

from advent_of_code.year_2024 import day_04


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("""\
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    """)

    def test_part_1(self) -> None:
        assert day_04.solve_part_1(self.__PUZZLE_INPUT) == 18

    def test_part_2(self) -> None:
        assert day_04.solve_part_2(self.__PUZZLE_INPUT) == 9
