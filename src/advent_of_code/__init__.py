import sys
from argparse import ArgumentParser
from importlib import import_module
from operator import itemgetter
from typing import Protocol, cast

EVENT_DAYS = set(range(1, 26))


class Solution(Protocol):
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
    solution: Solution | None = None

    try:
        solution = cast("Solution", import_module(f"advent_of_code.{year}.day_{day}.main"))
    except ModuleNotFoundError as e:
        sys.exit("The year has no available solutions!" if "day_" not in e.msg else "The day has no solution!")

    solution.main()
