#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser
from functools import partial


def path_ensure(arg: str, exists_ok: bool) -> Path:
    path = Path(arg)
    if (e := path.exists()) != exists_ok:
        print(f'ERROR: "{arg}" exists={e}')
        exit(1)
    return path


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--path", type=partial(path_ensure, exists_ok=False), required=True
    )
    parser.add_argument(
        "--code", type=partial(path_ensure, exists_ok=True), required=True
    )
    args = parser.parse_args()

    with open(args.code, "rt") as fp:
        code = fp.read().strip()

    with open(args.path, "wt") as fp:
        fp.write(code)


if __name__ == "__main__":
    main()
