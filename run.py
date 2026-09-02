#!/usr/bin/env python3
"""Entry point — fixes module resolution so `src.*` imports work without installing the package."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.cli import cli

if __name__ == "__main__":
    cli()
