# taken from https://github.com/pre-commit/pre-commit-hooks/blob/fd3bcbd96aff9c182ecbe5acd528d94ab88758de/pre_commit_hooks/util.py
# released under MIT license (https://github.com/pre-commit/pre-commit-hooks/blob/fd3bcbd96aff9c182ecbe5acd528d94ab88758de/LICENSE)

import subprocess
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Optional, Set


class CalledProcessError(RuntimeError):
    pass


def added_files() -> Set[str]:
    cmd = ("git", "diff", "--staged", "--name-only", "--diff-filter=A")
    return set(cmd_output(*cmd).splitlines())


def cmd_output(*cmd: str, retcode: Optional[int] = 0, **kwargs: Any) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


@contextmanager
def temporary_path():
    path = Path(str(uuid.uuid4()))
    try:
        yield path
    finally:
        path.unlink(missing_ok=True)
