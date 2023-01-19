from __future__ import annotations
from enum import Enum
from typing import Any, Dict, List

from detimer.matcher import Matcher
from detimer.rdiff_backup import rdiff_backup


class SpecialFileMode(Enum):
    DETECT = "detect"
    INCLUDE = "include"
    EXCLUDE = "exclude"


class Root:
    """Backup job"""

    def __init__(
        self,
        name: str,
        source: str,
        destination: str,
        special_files=SpecialFileMode.DETECT,
        matchers: List[Matcher] = None,
    ) -> None:
        if matchers is None:
            matchers = []

        self.name = name
        self.source = source
        self.destination = destination
        self.special_files = special_files
        self.matchers = matchers

    def backup(self, force=False, verbosity=3) -> None:
        options = []
        if force:
            options.append("--force")

        options.extend(["--verbosity", str(verbosity)])

        # Specify how to handle special files (if configured by user). If not
        # configured, rdiff-backup will choose based on the OS. Special files
        # are things like device files, sockets, symlinks, etc.
        if self.special_files == SpecialFileMode.INCLUDE:
            options.append("--include-special-files")
        elif self.special_files == SpecialFileMode.EXCLUDE:
            options.append("--exclude-special-files")

        options.extend(
            [
                arg
                for matcher in self.matchers
                for arg in [
                    "--exclude" if matcher.exclude else "--include",
                    f"'{matcher.pattern}'",
                ]
            ]
        )

        rdiff_backup(*options, self.source, self.destination)

    @staticmethod
    def parse(yaml: Dict[str, Any]) -> Root:
        """Parse from yaml entry for this root in the user's config"""

        if not isinstance(yaml, dict):
            raise TypeError("Root yaml must be a dictionary")

        if "name" not in yaml:
            raise ValueError("Each root must have a 'name'")

        if "src" not in yaml or "dest" not in yaml:
            raise ValueError("Each root must have 'src' and 'dest' paths")

        name = yaml["name"]
        src = yaml["src"]
        dest = yaml["dest"]

        if "special_files" in yaml:
            if yaml["special_files"] == "detect":
                special_files = SpecialFileMode.DETECT
            elif yaml["special_files"] == "include":
                special_files = SpecialFileMode.INCLUDE
            elif yaml["special_files"] == "exclude":
                special_files = SpecialFileMode.EXCLUDE
            else:
                raise ValueError(f"Invalid special_files mode: {yaml['special_files']}")
        else:
            special_files = SpecialFileMode.DETECT

        if "match" in yaml:
            matchers = yaml["match"].strip().split("\n")
            matchers = [
                Matcher.parse(matcher.strip(), source=src) for matcher in matchers
            ]
        else:
            matchers = None

        return Root(name, src, dest, special_files, matchers)
