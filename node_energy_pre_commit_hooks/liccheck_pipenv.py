import argparse
from typing import Optional, Sequence

from node_energy_pre_commit_hooks.utils import (
    CalledProcessError,
    cmd_output,
    temporary_path,
)


def run_liccheck_against_pipfile_lock(
    filenames: Sequence[str], strategy_file: str
) -> int:
    if "Pipfile.lock" not in set(filenames):
        return 0

    with temporary_path() as requirements_path:
        requirements_path.write_text(cmd_output("pipenv", "lock", "--requirements"))
        args = ("liccheck", "-s", strategy_file, "-r", requirements_path)
        try:
            cmd_output(*args)
        except CalledProcessError:
            raise CalledProcessError(
                f"liccheck pre-commit hook failed. Re-run for more details: {' '.join(args)}"
            )
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames", nargs="*", help="Filenames pre-commit believes are changed.",
    )
    parser.add_argument(
        "--strategy", type=str, default="strategy.ini", help="Path to strategy file",
    )

    args = parser.parse_args(argv)
    return run_liccheck_against_pipfile_lock(args.filenames, args.strategy)


if __name__ == "__main__":
    exit(main())
