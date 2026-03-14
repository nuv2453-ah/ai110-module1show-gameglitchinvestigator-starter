"""Pytest configuration for the Game Glitch Investigator project.

Adds the project root to sys.path so tests can import root-level modules without
requiring PYTHONPATH to be set externally.

Essentially, it modifies the Python path at runtime to include the project root directory, allowing for tests to import modules
specifically, it allows for Python to import "from logic_utils import parse_guess" because earlier the terminal was giving errors
"""

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
