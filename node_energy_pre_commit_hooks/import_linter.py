import argparse

from typing import Optional, Sequence

from importlinter.cli import lint_imports


def run_import_linter(
    filenames: Sequence[str], config_file: str
) -> int:
    if len(filenames) == 0:
        return 0

    return lint_imports(config_filename=config_file)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames", nargs="*", help="Filenames pre-commit believes are changed.",
    )
    parser.add_argument(
        "--config-file", type=str, default=".importlinter", help="Path to import linter config file",
    )

    args = parser.parse_args(argv)
    return run_import_linter(args.filenames, args.config_file)


if __name__ == "__main__":
    exit(main())
