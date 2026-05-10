"""
generate.py

Generate synthetic Python host programs using Hypothesmith.

Outputs are saved into:
    generated_programs/hosts/

Example:
    python -m src.generate
"""

import ast
import os
from pathlib import Path

from hypothesis import settings
from hypothesmith import from_grammar

# --------------------------------------------------
# Configuration
# --------------------------------------------------

OUTPUT_DIR = Path("generated_programs/hosts")

NUM_PROGRAMS = 100
MAX_ATTEMPTS = 500

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Helpers
# --------------------------------------------------

def valid_python(src: str) -> bool:
    """
    Ensure generated code parses successfully.
    """
    try:
        ast.parse(src)
        return True
    except Exception:
        return False


def save_program(code: str, index: int) -> None:
    """
    Save generated host program to disk.
    """
    out_path = OUTPUT_DIR / f"host_{index}.py"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(code)


# --------------------------------------------------
# Main generation loop
# --------------------------------------------------

@settings(
    max_examples=MAX_ATTEMPTS,
    deadline=None,
)
def generate_hosts():
    """
    Generate NUM_PROGRAMS valid host programs.
    """

    strategy = from_grammar()

    generated = 0
    attempts = 0

    while generated < NUM_PROGRAMS and attempts < MAX_ATTEMPTS:

        attempts += 1

        try:
            code = strategy.example()

            if not isinstance(code, str):
                continue

            if len(code.strip()) == 0:
                continue

            # Validate syntax
            if not valid_python(code):
                continue

            save_program(code, generated)

            generated += 1

            print(f"[+] Generated host_{generated}.py")

        except Exception:
            continue

    print()
    print("===================================")
    print(f"Generated hosts : {generated}")
    print(f"Total attempts  : {attempts}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("===================================")


# --------------------------------------------------
# Entry point
# --------------------------------------------------

if __name__ == "__main__":
    generate_hosts()