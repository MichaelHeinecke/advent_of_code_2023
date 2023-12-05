from typing import List


def get_input_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]
