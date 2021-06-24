"""Upload plugin rsync."""
from pathlib import Path

from ..utils import run_command


def upload(wheels_port: str, local: Path, remote: str) -> None:
    """Upload wheels from folder to remote rsync server."""
    run_command(
        f"rsync e 'ssh -p {wheels_port}' --human-readable --recursive --progress --checksum {local}/* {remote}/",
    )
