"""
A constant-memory implementation of the cat command-line utility.
"""

import sys

CHUNK_SIZE = 64 * 1024


def cat(file):
    """Copy a binary file-like object to standard output in fixed-size chunks."""
    output = sys.stdout.buffer

    while True:
        data = file.read(CHUNK_SIZE)
        if not data:
            break
        output.write(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as file:
                cat(file)
    else:
        cat(sys.stdin.buffer)
