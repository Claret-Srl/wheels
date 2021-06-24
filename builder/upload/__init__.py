"""Supported upload function."""
from pathlib import Path
from importlib import import_module


def run_upload(plugin: str, port: str, local: Path, remote: str) -> None:

    """Load a plugin and start upload."""
    plugin = import_module(f".{plugin}", "builder.upload")

    # Run upload
    plugin.upload(port, local, remote)
