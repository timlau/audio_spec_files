#!/usr/bin/python
import argparse
import subprocess


def find_dep(dep: str):
    # if dep.startswith("lib"):
    #     dep = dep[3:]
    if dep.endswith("-dev"):
        dep = dep[:-4]
    cmd = f"dnf repoquery -q {dep}-devel*.x86_64"
    # print(f"running: {cmd}")
    result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
    found = result.stdout.decode("utf-8").split("\n")
    for pkg in found:
        if pkg:
            cmd = f"dnf repoquery -q --provides {pkg}"
            result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
            print(f"{pkg} Provides:")
            provides = result.stdout.decode("utf-8").split("\n")
            for provide in provides:
                if provide:
                    print(f" --> {provide}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("deps", nargs="*", default=[])
    args = parser.parse_args()
    for dep in args.deps:
        print(f"lookin for dep: {dep}")
        find_dep(dep)


if __name__ == "__main__":
    main()
