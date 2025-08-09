from advent_of_code.year_2024 import day_03


class TestSolution:
    def test_part_1(self) -> None:
        puzzle_in = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

        assert day_03.solve_part_1(puzzle_in) == 161

    def test_part_2(self) -> None:
        puzzle_in = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

        assert day_03.solve_part_2(puzzle_in) == 48
