"""Tests the functionality of a 2-approximation to metric TSP."""
# CSC 349 Assignment 5
# Feel free to add additional tests!
from __future__ import annotations

import os
import re
import subprocess
import unittest

from graph import Graph

OUTPUT_RE = re.compile(
    r"\AHamiltonian cycle of weight (?P<weight>\d+):\n"
    r"(?P<cycle>(?:\d+, )*\d+)\n\Z"
)


def prepare_shell_files(*files: str) -> None:
    """Set the execute bits on given shell files.

    Note: This will not work on Windows.

    Args:
        files: the shell filename
    """
    for file in files:
        os.chmod(file, os.stat(file).st_mode | 0o111)


def run_compile(timeout: float = 3.0) -> None:
    """Run the local file compile.sh.

    Args:
        timeout: length of time (in seconds) to wait
    """
    subprocess.run(
        ["sh", "compile.sh"],
        timeout=timeout,
        check=True,
    )


def run_code(input_file: str, timeout: float = 0.5) -> tuple[str, str]:
    """Run the local file run.sh and return the output.

    Args:
        input_file:  name of the input file for run.sh
        timeout: length of time (in seconds) to wait

    Returns:
        The stdout and stderr from running the script.
    """
    result = subprocess.run(
        ["./run.sh", input_file],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        check=True,
        text=True,
    )

    return result.stdout, result.stderr


def parse_cycle(raw_output: str) -> tuple[int, tuple[int, ...]]:
    """Parse the stdout into a weight and a cycle.

    Args:
        output: the stdout from run.sh

    Returns:
        The weight of the cycle and the cycle itself
    """
    m = OUTPUT_RE.fullmatch(raw_output)

    if not m:
        raise ValueError("Could not parse output")

    weight = int(m["weight"])
    cycle = tuple(int(x) for x in m["cycle"].split(", "))

    return weight, cycle


class TSPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        prepare_shell_files("compile.sh", "run.sh")
        run_compile()

    def assert_hamiltonian_cycle_with_weight(
        self, cycle: tuple[int, ...], weight: int, input_file: str
    ) -> None:
        graph = Graph.from_file(input_file)

        self.assertEqual(
            cycle[0],
            cycle[-1],
            f"On input {input_file!r}, your cycle does not start and end at "
            "the same vertex",
        )

        self.assertCountEqual(
            cycle[1:],
            graph,
            f"On input {input_file!r}, your cycle has extra or missing "
            "vertices",
        )

        actual_weight = sum(
            graph[cycle[i]][cycle[i + 1]] for i in range(len(cycle) - 1)
        )

        self.assertEqual(
            weight,
            actual_weight,
            f"On input {input_file!r}, your cycle does not have the weight "
            "specified",
        )

    def assert_approximation(self, input_file: str, optimal: int) -> None:
        out, err = run_code(input_file)

        self.assertEqual(
            err, "", f"On input {input_file!r}, your code prints to stderr"
        )

        self.assertRegex(
            out,
            OUTPUT_RE,
            f"On input {input_file!r}, your output is in the wrong format.",
        )

        try:
            weight, cycle = parse_cycle(out)
        except ValueError as e:
            self.fail(f"On input {input_file!r}: {e}")

        self.assertLessEqual(
            weight,
            2 * optimal,
            f"On input {input_file!r}, your algorithm is worse than a "
            "2-approximation",
        )

        self.assert_hamiltonian_cycle_with_weight(cycle, weight, input_file)

    def test_in1(self):
        self.assert_approximation("test_files/in1.txt", 21)

    def test_in2(self):
        self.assert_approximation("test_files/in2.txt", 3)

    def test_in3(self):
        self.assert_approximation("test_files/in3.txt", 8)


if __name__ == "__main__":
    unittest.main()
