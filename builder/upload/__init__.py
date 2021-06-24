"""Supported upload function."""
from pathlib import Path
from importlib import import_module


def run_upload(plugin: str, wheels_port: str, local: Path, remote: str, ftp_host: str, ftp_user: str, ftp_password: str, ftp_remote: str, ftp_mirror_options: str) -> None:

    """Load a plugin and start upload."""
    plugin = import_module(f".{plugin}", "builder.upload")

    # Run upload
    if plugin == "rsync":
        plugin.upload(wheels_port, local, remote)
    else:    
        plugin.upload(local, ftp_host, ftp_user, ftp_password, ftp_remote, ftp_mirror_options)
