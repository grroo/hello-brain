#!/usr/bin/env python3
"""tiny — a very small CLI. Exists so the brain team has something to work on.

Pattern for every command: a `cmd_<name>(args) -> str` function that returns
the output, registered in `build_parser()`. `run(argv)` returns the string, and
`main()` prints it. Tests call `run()` and never touch stdout.
"""
import argparse
import sys

VERSION = "0.1.0"


def cmd_version(args):
    return f"tiny {VERSION}"


def cmd_shout(args):
    text = " ".join(args.words)
    return text.upper() + "!"


def build_parser():
    parser = argparse.ArgumentParser(prog="tiny", description="a very small CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_version = sub.add_parser("version", help="print the version")
    p_version.set_defaults(func=cmd_version)

    p_shout = sub.add_parser("shout", help="repeat words, loudly")
    p_shout.add_argument("words", nargs="+", help="words to shout")
    p_shout.set_defaults(func=cmd_shout)

    return parser


def run(argv):
    """Parse argv (without the program name) and return the command's output."""
    args = build_parser().parse_args(argv)
    return args.func(args)


def main():
    print(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
