#!/usr/bin/env python

import argparse
import json
from subprocess import getoutput
from pathlib import Path


def parse_args() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to backend-root")
    parser.add_argument('-c', '--contexts', nargs='+', default=[])
    args = parser.parse_args()
    path = args.path
    contexts = set(args.contexts)
    return (Path(path), contexts)


def without_context(context: str, contexts: set[str]):
    ctxts = set(contexts)
    ctxts.discard(context)
    return ctxts


def reorder(context_violations, path):
    dct = {key: {} for key in context_violations}
    for package, contents in context_violations.items():
        for pkg, files in contents.items():
            for file in files:
                file = str(path/file)
                if file not in dct[package]:
                    dct[package][file] = []
                dct[package][file].append(pkg)
    return dct


def main():
    path, contexts = parse_args()
    context_violations = {}
    for context in contexts:
        context_violations[context] = {}
        for ctx in without_context(context, contexts):
            # Exclude lines that contain these words (hint to events)
            exclude = "|".join(["payloads", "models"])
            cmd = f"rg --pcre2 -l -g '*.java' 'import.*(?!.*(?>{exclude}))' {path/context}/"
            out = getoutput(cmd).split()
            context_violations[context][ctx] = out

    context_violations = reorder(context_violations, path)
    with open("context_violations.json", "w") as file:
        json.dump(context_violations, file, sort_keys=True, indent=2)


if __name__ == "__main__":
    main()
