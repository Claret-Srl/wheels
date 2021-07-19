"""Upload plugin lftp."""
from pathlib import Path

from ..utils import run_command


def upload(
    local: Path,
    ftp_host: str,
    ftp_user: str,
    ftp_password: str,
    ftp_remote: str,
    ftp_mirror_options: str,
) -> None:
    """Upload wheels from folder to remote lftp server."""
    run_command(
        f'lftp {ftp_host} -u {ftp_user},{ftp_password} -e "mirror {ftp_mirror_options} {local}/ {ftp_remote}; quit"',
    )
