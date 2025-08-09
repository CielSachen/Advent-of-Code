import argparse
import calendar
import datetime
import importlib
import pathlib
import textwrap
from os import path
from typing import Protocol, cast

from advent_of_code import year_2024


class Solution(Protocol):
    TITLE: str

    def solve_part_1(self, puzzle_in: str) -> int: ...

    def solve_part_2(self, puzzle_in: str) -> int: ...


def main() -> None:
    evt_days = tuple(range(1, 26))

    parser = argparse.ArgumentParser(description="Shows the answers to Advent of Code puzzles")
    parser.add_argument(
        "-y",
        "--year",
        nargs="+",
        type=int,
        required=True,
        help="set the years to get the puzzles from",
        metavar="<year>",
    )
    parser.add_argument(
        "-d",
        "--day",
        nargs="+",
        type=int,
        choices=evt_days,
        required=True,
        help="set the days to show the answers of",
        metavar=f"{{{evt_days[0]}...{evt_days[-1]}}}",
    )

    args = parser.parse_args()

    for i, year in enumerate(args.year):
        for j, day in enumerate(args.day):
            sol: Solution

            try:
                sol = cast("Solution", importlib.import_module(f"advent_of_code.year_{year}.day_{day:02d}"))
            except ModuleNotFoundError as e:
                if "day_" in e.msg:
                    print(f"The puzzle for day '{day}' of the year '{year}' was not solved")

                    continue

                if (
                    year <= (curr_date := datetime.datetime.now(datetime.UTC)).year
                    and curr_date.month < calendar.DECEMBER
                ):
                    print(f"The puzzles for the year '{year}' are not yet out")
                else:
                    print(f"The puzzles for the year '{year}' were not solved")

                break

            print(f"--- Day {day}: {sol.TITLE} ---")

            print()

            try:
                puzzle_in = pathlib.Path(path.join("inputs", f"year_{year}", f"day_{day:02d}.txt")).read_text(
                    encoding="utf-8"
                )

                print(
                    textwrap.dedent(f"""\
                        Part 1 Puzzle Answer: {sol.solve_part_1(puzzle_in)}
                        Part 2 Puzzle Answer: {sol.solve_part_2(puzzle_in)}\
                    """)
                )
            except FileNotFoundError:
                print("Error: The puzzle's input file could not be found")
            except year_2024.day_06.NoStartingPositionError as e:
                print(f"Error: {e}")

            if j < len(args.day) - 1:
                print()

        if i < len(args.year) - 1:
            print()
