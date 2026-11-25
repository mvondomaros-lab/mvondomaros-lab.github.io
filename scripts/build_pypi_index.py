"""Build the static PEP 503 index in public/pypi from the wheels and sdists in pypi/.

simple503 only indexes wheels (it globs ``**/*.whl`` and reads each wheel's METADATA),
so this script lets it handle the wheels and then adds the ``.tar.gz`` sdists to the
same project pages, with the project name and Requires-Python taken from their PKG-INFO.

Usage: python scripts/build_pypi_index.py SOURCE TARGET BASE_URL
"""

import hashlib
import shutil
import sys
import tarfile
from email.parser import HeaderParser
from operator import attrgetter
from pathlib import Path

from natsort import natsorted
from shippinglabel import normalize
from simple503 import WheelFile, generate_index, generate_project_page, make_simple


def read_pkg_info(sdist: Path) -> dict:
    """Return the headers of the top-level ``<name>-<version>/PKG-INFO`` of an sdist."""
    with tarfile.open(sdist) as tar:
        for member in tar.getmembers():
            parts = member.name.split("/")
            if len(parts) == 2 and parts[1] == "PKG-INFO" and member.isfile():
                text = tar.extractfile(member).read().decode("utf-8")
                return HeaderParser().parsestr(text)
    raise FileNotFoundError(f"PKG-INFO not found in {sdist}")


def main(source: str, target: str, base_url: str) -> None:
    source_dir, target_dir = Path(source), Path(target)
    projects = make_simple(source_dir, target_dir, base_url, sort=True, copy=True)

    for sdist in sorted(source_dir.glob("*.tar.gz")):
        pkg_info = read_pkg_info(sdist)
        project_dir = target_dir / normalize(pkg_info["Name"])
        project_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(sdist, project_dir / sdist.name)
        projects.setdefault(pkg_info["Name"], []).append(
            WheelFile(
                filename=f"{project_dir.name}/{sdist.name}",
                wheel_hash=hashlib.sha256(sdist.read_bytes()),
                requires_python=pkg_info.get("Requires-Python"),
            )
        )

    # Rewrite the pages simple503 generated, now including the sdists.
    (target_dir / "index.html").write_text(str(generate_index(projects.keys(), base_url)))
    for name, files in projects.items():
        page = generate_project_page(
            name, natsorted(files, key=attrgetter("filename"), reverse=True), base_url
        )
        (target_dir / normalize(name) / "index.html").write_text(str(page))


if __name__ == "__main__":
    main(*sys.argv[1:])
