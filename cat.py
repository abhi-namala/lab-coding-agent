'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 64 * 1024


def cat(file):
    out = sys.stdout.buffer
    while True:
        data = file.read(CHUNK_SIZE)
        if not data:
            break
        out.write(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as file:
                cat(file)
    else:
        cat(sys.stdin.buffer)
