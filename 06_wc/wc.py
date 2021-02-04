import argparse
import os
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Word Count", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "file",
        nargs="*",
        help="input file(s)",
        metavar="File",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
    )
    return parser.parse_args()


def main():
    args = get_args()

    for fh in args.file:
        lines = 0
        words = 0
        chars = 0
        for line in fh:
            lines += 1
            cur_line = line
            line_arr = cur_line.split()
            words += len(line_arr)
            chars += len(cur_line)
        print(f"{lines:8}{words:8}{chars:8} {fh.name}")


if __name__ == "__main__":
    main()