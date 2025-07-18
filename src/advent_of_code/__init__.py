import sys
from argparse import ArgumentParser
from importlib import import_module
from operator import itemgetter
from typing import Protocol, cast

EVENT_DAYS = tuple(range(1, 26))


class Solution(Protocol):
    def solve_part_one(self, puzzle_in: str) -> None:
        pass

    def solve_part_two(self, puzzle_in: str) -> None:
        pass

    def main(self) -> None:
        pass


def main() -> None:
    parser = ArgumentParser()

    parser.add_argument("year", type=int, help="the year of the Advent of Code event")
    parser.add_argument(
        "day", type=int, choices=EVENT_DAYS, help="the day to show the puzzle answers of", metavar="day"
    )

    year: int
    day: int
    year, day = itemgetter("year", "day")(vars(parser.parse_args()))
    sol: Solution | None = None

    try:
        sol = cast("Solution", import_module(f"advent_of_code.{year}.day_{day}.main"))
    except ModuleNotFoundError as e:
        sys.exit("The year has no available solutions!" if "day_" not in e.msg else "The day has no solution!")

    sol.main()
