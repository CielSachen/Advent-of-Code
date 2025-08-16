import textwrap

from advent_of_code.year_2024 import day_05


class TestSolution:
    __PUZZLE_INPUT = textwrap.dedent("""\
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
    """)

    def test_part_1(self) -> None:
        assert day_05.solve_part_1(self.__PUZZLE_INPUT) == 143

    def test_part_2(self) -> None:
        assert day_05.solve_part_2(self.__PUZZLE_INPUT) == 123
