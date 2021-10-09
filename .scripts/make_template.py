#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser


CODE = """
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define output_t void

output_t solve(int tc) {
    ;

    return;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int tc;

    //tc = 1;
    cin >> tc;

    while (tc--) {
        solve(tc);
    }

    return 0;
}
""".strip()


def path_ensure_new(arg: str) -> Path:
    path = Path(arg)
    if path.exists():
        print(f'ERROR: "{arg}" already exists.')
        exit(1)
    return path


parser = ArgumentParser()
parser.add_argument("--path", type=path_ensure_new, required=True)
args = parser.parse_args()

with open(args.path, "wt") as fp:
    fp.write(CODE)
