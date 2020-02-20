import argparse
from typing import Optional, Sequence

from node_energy_pre_commit_hooks.utils import added_files, cmd_output, temporary_path


def run_liccheck_against_pipfile_lock(filenames: Sequence[str], strategy_file: str) -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    print("input", filenames)
    print("added", added_files())
    if "Pipfile.lock" not in (added_files() & set(filenames)):
        return 0

    with temporary_path() as requirements_path:
        requirements_path.write_text(cmd_output("pipenv", "lock", "--requirements"))
        cmd_output("liccheck", "-s", strategy_file, "-r", requirements_path)
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
