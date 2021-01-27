"""Tox hook implementations."""
from __future__ import print_function

import logging
import os
import subprocess
import sys

try:
    from tox import hookimpl

    @hookimpl
    def tox_configure(config):
        """..."""
        if os.path.isfile("bindep.txt"):
            cmd = ["bindep", "-b"]
            # determine profiles
            result = subprocess.run(
                ["bindep", "--profiles"],
                check=False,
                universal_newlines=True,
                stdout=subprocess.PIPE,
            )
            if result.returncode:
                print("Bindep failed to list profiles: %s", result.stdout)
                sys.exit(result.returncode)
            lines = result.stdout.splitlines()
            profiles = lines[lines.index("Configuration profiles:") + 1 :]
            if "test" in profiles:
                cmd.append("test")

            result = subprocess.run(
                cmd,
                check=False,
                universal_newlines=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            if result.returncode:
                print(
                    "Running '%s' returned %s, likely missing "
                    "system dependencies." % (" ".join(cmd), result.returncode)
                )
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr, file=sys.stderr)
                sys.exit(result.returncode)


except ImportError:
    # tox4
    logging.error("tox-bindep disabled itself as it does not support tox4 yet.")
