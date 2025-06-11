import subprocess
import sys
import os
import pytest


# Path to add.py script
SCRIPT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "src/add.py"))


def run_add(args):
    """Runs add.py with the given arguments and returns CompletedProcess."""
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True,
        text=True
    )


def test_add_integers():
    """3 + 5 = 8.0 (float)."""
    result = run_add(["3", "5"])
    assert result.returncode == 0
    assert result.stdout.strip() == "8.0"


def test_add_floats():
    """2.5 + 4.1 = 6.6."""
    result = run_add(["2.5", "4.1"])
    assert result.returncode == 0
    # we are comparing as a string, because print() returns exactly '6.6'
    assert result.stdout.strip() == "6.6"


def test_invalid_input():
    """Non-number as an argument should end with an error (exit code != 0)."""
    result = run_add(["foo", "1"])
    assert result.returncode != 0
    # argparse will throw something like “invalid float value”
    assert "invalid float value" in result.stderr
